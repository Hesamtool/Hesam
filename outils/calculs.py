# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:44:39 2019

@author: Utilisateur
"""
import math
import os
import stl
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from .models import Prototype, Material_proto, Material_support, Result, Printer, Level
from shapely.geometry import Polygon

# find the max dimensions, so we can know the bounding box, getting the height,
# width, length (because these are the step size)...
    
def find_mins_maxs(obj):
    """Determines the min and max point in 3 directions of the stl file"""
    minx = maxx = miny = maxy = minz = maxz = None
    for points in obj.vectors:
        for p in points :
        # p contains (x, y, z)
            if minx is None:
                minx = p[stl.Dimension.X]
                maxx = p[stl.Dimension.X]
                miny = p[stl.Dimension.Y]
                maxy = p[stl.Dimension.Y]
                minz = p[stl.Dimension.Z]
                maxz = p[stl.Dimension.Z]
            else:
                maxx = max(p[stl.Dimension.X], maxx)
                minx = min(p[stl.Dimension.X], minx)
                maxy = max(p[stl.Dimension.Y], maxy)
                miny = min(p[stl.Dimension.Y], miny)
                maxz = max(p[stl.Dimension.Z], maxz)
                minz = min(p[stl.Dimension.Z], minz)
    return minx, maxx, miny, maxy, minz, maxz

def plot_stl(obj, name, stra) :
    """Plot of STL and Bounding box"""
    matplotlib.use("Agg")
    figure = plt.figure(facecolor="white")
    axes = mplot3d.Axes3D(figure)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(obj.vectors, facecolors='purple', linewidths = 1)) #Plot the STL part
    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(obj) #Plot the bounding box
    xs = [minx, minx, minx, minx, maxx, maxx, maxx, maxx]
    ys = [miny, miny, maxy, maxy, miny, miny, maxy, maxy]
    zs = [minz, maxz, minz, maxz, minz, maxz, minz, maxz]
    axes.scatter(xs, ys, zs, c='orange')
    axes.set_xticklabels([])
    axes.set_yticklabels([])
    axes.set_zticklabels([])
    scale = obj.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    plt.savefig("media/stl/" + str(name) + "_" + str(stra) + ".png", transparent = True)

def volume_bounding_box(obj) : 
    """Calculation the volume of the bounding box"""
    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(obj)
    Vol = (maxx-minx)*(maxy-miny)*(maxz-minz)
    return Vol

def volume_stl(obj) :
    """Calculation the volume of the STL part"""
    volume, cog, inertia = obj.get_mass_properties()
    return volume
        
def val_elements(obj, plans) : 
    """Calculation of the support volume for each triangle according to the projection plane without the filling"""
    triangles = obj.vectors
    normals = normal_vectors(triangles)
    barycenter = barycenter_coordinates(plans, triangles)
    pro_part = projections_coordinates(plans, triangles)
    data_ele = []
    lst_surf =[]
    for m, support in enumerate (plans) :
        elements = []
        polygons = polygons_coordinates(pro_part, m)
        axe = support[2]
        angles = []
        sum_surf = 0
        for l,tri in enumerate(triangles) :
            angles.append(angle_degree(support[0], normals[l]))
        for n, triangle in enumerate(triangles) :
            if angles[n] <= 90 :
                vol_ele = 0        
            else :
                poly_inter = []         
                for p, polygon in enumerate(polygons) :
                    if angles[p] < 90 :                
                        if polygons[n].intersects(polygon) :
                            poly_inter.append(p)
                bary_tri = barycenter[m][n][axe]
                bary_clo = barycenter[m][poly_inter[0]][axe]
                for val in poly_inter :
                    bary_pol = barycenter[m][val][axe]
                    bary_clo = 'none'
                    if val != n and ((-1)**(m))*bary_tri > ((-1)**(m))*bary_pol :
                        if bary_clo == 'none':
                            bary_clo = bary_pol
                        elif abs(bary_tri - bary_pol) < abs(bary_tri - bary_clo) :
                            bary_clo = bary_pol
                if bary_clo =='none' :
                    surf = np.linalg.norm(np.cross(pro_part[m][n][0]-pro_part[m][n][1], pro_part[m][n][2]-pro_part[m][n][1]))/2
                    sum_surf = sum_surf + surf
                    lmoy = abs(bary_tri-support[1][axe])
                    vol_ele = lmoy * surf
                else :
                    lmoy = abs(bary_tri-bary_pol)
                    vol_ele = lmoy * np.linalg.norm(np.cross(pro_part[m][n][0]-pro_part[m][n][1], pro_part[m][n][2]-pro_part[m][n][1]))/2
            elements.append([pro_part[m][n], vol_ele, angles[n]])
        data_ele.append(elements)
        lst_surf.append(sum_surf)
    return data_ele, lst_surf
 
def angle_degree (vect1, vect2) :
    """Calculation of the angle between 2 vectors"""
    angle = np.degrees(np.arccos(np.dot(vect1, vect2)/(np.linalg.norm(vect1)*np.linalg.norm(vect2))))
    return angle

def normal_vectors(triangles) :
    """Calculation of the normal vectors"""
    normals = []
    for triangle in triangles :
        vec = np.cross(triangle[1]-triangle[0], triangle[2]-triangle[0])
        normals.append(vec/np.linalg.norm(vec))
    return normals

def barycenter_coordinates(plans, triangles) :
    """Determines the barycentre of all triangles"""
    barycenters_plans = []
    for support in plans :
        barycenters = []
        for pt1, pt2, pt3 in triangles :
            bary = [((np.float64(pt1[0])+np.float64(pt2[0])+np.float64(pt3[0]))/3), ((np.float64(pt1[1])+np.float64(pt2[1])+np.float64(pt3[1]))/3), ((np.float64(pt1[2])+np.float64(pt2[2])+np.float64(pt3[2]))/3)]
            barycenters.append(bary)
        barycenters_plans.append(barycenters)
    return barycenters_plans

def projections_coordinates(plans, triangles) :
    """Deterines the projections of all points"""
    pro_part = []
    for support in plans :
        pro_tris = []
        for triangle in triangles :
            pro_pts = []
            for point in triangle :
                vect0 = np.array(support[0])
                vect1 = np.array(support[1])
                pro_pts.append(point - (np.vdot(vect0, point)-np.vdot(vect0, vect1))/np.vdot(vect0, vect0)*vect0)
            pro_tris.append(pro_pts)
        pro_part.append(pro_tris)
    return pro_part
        
def plans_projection(obj):
    """Select projection plans"""
    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(obj)
    plans = np.array([[[0,0,1],[0,0,minz],2],[[0,0,-1],[0,0,maxz],2],[[0,1,0],[0,miny,0],1],[[0,-1,0],[0,maxy,0],1],[[1,0,0],[minx,0,0],0],[[-1,0,0],[maxx,0,0],0]])
    return plans

def polygons_coordinates(pro_part, index) :
    pro_tris =  pro_part[index]
    polygons = []
    for triangle in pro_tris :
        if index == 0 or index == 1 :
            polygons.append(Polygon(triangle))
        elif index == 2 or index == 3 :
            polygons.append(Polygon([[triangle[0][2],triangle[0][0],triangle[0][1]],[triangle[1][2],triangle[1][0],triangle[1][1]],[triangle[2][2],triangle[2][0],triangle[2][1]]]))
        elif index == 4 or index == 5 :
            polygons.append(Polygon([[triangle[0][1],triangle[0][2],triangle[0][0]],[triangle[1][1],triangle[1][2],triangle[1][0]],[triangle[2][1],triangle[2][2],triangle[2][0]]]))
    return polygons
        
def list_volume_suppo(data_ele, alpha):
    """Sum of the volume support of each triangle according to the angle alpha without the filling"""
    lst_vol_sup_0 = []
    lst_vol_sup_68 = []
    for support in data_ele :
        volume_0 = 0
        volume_68 = 0
        for element in support :
            if element[2] >= (alpha+90):
                volume_68 += element[1]
            volume_0 += element[1]
        lst_vol_sup_68.append(volume_68)
        lst_vol_sup_0.append(volume_0)
    return lst_vol_sup_0, lst_vol_sup_68

def transform(obj, vector, plan, name, stra):
    """Transform the part"""
    
    if np.all(vector==[0, 0, 1]) == True:
        pass
    elif np.all(vector==[0, 0, -1]) == True:
        obj.rotate([1.0,0.0,0.0], math.radians(180))
    elif np.all(vector==[0, 1, 0]) == True:
        obj.rotate([1.0,0.0,0.0], math.radians(-90))
    elif np.all(vector==[0, -1, 0]) == True:
        obj.rotate([1.0,0.0,0.0], math.radians(90))
    elif np.all(vector==[1, 0, 0]) == True:
        obj.rotate([1.0,0.0,0.0], math.radians(-90))
    elif np.all(vector==[-1, 0, 0]) == True:
        obj.rotate([1.0,0.0,0.0], math.radians(90))
    plot_stl(obj, name, stra)
    
def choice_printers():
    """Select printers according to the selection of the user""" 
    lst_printer=[]
    prototype = Prototype.objects.order_by('-date')[0]
    lst_material_yes =[]
    lst_material_yes.append([mat.title for mat in prototype.material_yes.all()])
    lst_material_no =[]
    lst_material_no.append([mat.title for mat in prototype.material_no.all()])
    lst_technology_yes =[]
    lst_technology_yes.append([tec.title for tec in prototype.technology_yes.all()])
    lst_technology_no =[]
    lst_technology_no.append([tec.title for tec in prototype.technology_no.all()])
    for pri,printer in enumerate(Printer.objects.all()):
        if (len(lst_technology_yes[0])==0 or str(printer.technology) in lst_technology_yes[0]) \
        and (len(lst_material_yes[0])==0 or str(printer.mate_proto) in lst_material_yes[0]) \
        and (not prototype.colour or prototype.colour == 'Monochrome' or prototype.colour == str(printer.colour)) \
        and (not prototype.thermal_resistance or prototype.thermal_resistance == str(printer.thermal_resistance)) \
        and (not prototype.optical_resistance or prototype.optical_resistance == str(printer.optical_resistance)) \
        and (not str(printer.mate_proto) in lst_material_no[0]) \
        and (not prototype.printing_speed or prototype.printing_speed == str(printer.printing_speed))\
        and (not str(printer.technology) in lst_technology_no[0]):
            lst_printer.append(pri)
    return lst_printer


def optimisation (vol_stl, lst_printers, vol_tot_support_0, vol_tot_support_68, rack_surf_0, rack_surf_68) :
    """Determines the best orientation according to the limit angle and strategy selection"""
    price_cost = 0
    index_pri_cost = 0
    vol_sup_cost = 0
    price_mate = 0
    index_pri_mate = 0
    vol_sup_mate = 0
    vol_real_mate = 0
    vol_real_cost = 0
    overhang_mate = 0
    overhang_cost = 0
    for pri in lst_printers:
        printer = Printer.objects.all()[pri]
        over = np.float64(printer.overhang_angle_label)
        if over == 0 :
            rack_surf = rack_surf_0
            vol_tot_support = vol_tot_support_0
            overhang = 0
        else :
            rack_surf = rack_surf_68
            vol_tot_support = vol_tot_support_68
            overhang = 68
        price_suppo = np.float64(Material_support.objects.get(title = printer.mate_suppo).price)
        price_proto = np.float64(Material_proto.objects.get(title = printer.mate_proto).price)
        dens_suppo = np.float64(Material_support.objects.get(title = printer.mate_suppo).density)
        dens_proto = np.float64(Material_proto.objects.get(title = printer.mate_proto).density)
        lost_suppo = np.float64(printer.qtt_material_suppo_lost)
        lost_proto = np.float64(printer.qtt_material_proto_lost)
        fill_suppo = np.float64(printer.infill_dens_suppo)
        rack_fill = np.float64(printer.rack_filling)
        rack_height = np.float64(printer.rack_height)
        vol_support = vol_tot_support * fill_suppo / 100
        vol_real_proto = vol_stl * infill_proto(printer)
        vol_rack = rack_surf * rack_height * rack_fill/100
        print(vol_support)
        print(vol_rack)
        price = (vol_real_proto + lost_proto) * price_proto * dens_proto + (vol_support + lost_proto + vol_rack) * dens_suppo * price_suppo
        if price_cost == 0 or price_mate == 0 :
            overhang_mate = overhang
            overhang_cost = overhang
            price_mate = price
            price_cost = price
            index_pri_cost = pri
            index_pri_mate = pri
            vol_sup_cost = vol_support + vol_rack
            vol_sup_mate = vol_support + vol_rack
            vol_real_mate = vol_real_proto
            vol_real_cost = vol_real_proto
        else :
            # Optimisation of cost
            if price < price_cost :
                price_cost = price
                index_pri_cost = pri
                vol_sup_cost = vol_support + vol_rack
                vol_real_cost = vol_real_proto
                overhang_cost = overhang
            elif price == price_cost and vol_support < vol_sup_cost :
                price_cost = price
                index_pri_cost = pri
                vol_sup_cost = vol_support + vol_rack
                vol_real_cost = vol_real_proto
                overhang_cost = overhang
            # Optimisation of material
            if vol_support < vol_sup_mate :
                price_mate = price
                index_pri_mate = pri
                vol_sup_mate = vol_support + vol_rack
                vol_real_mate = vol_real_proto
                overhang_mate = overhang
            elif vol_support == vol_sup_mate and price < price_mate :
                price_mate = price
                index_pri_mate = pri
                vol_sup_mate = vol_support + vol_rack
                vol_real_mate = vol_real_proto
                overhang_mate = mate
    return round(vol_sup_cost,2), round(price_cost,2), index_pri_cost, vol_real_cost, overhang_cost, round(vol_sup_mate,2), round(price_mate,2), index_pri_mate, vol_real_mate, overhang_mate

def layer_height(printer):
    """Determines the best layer height according to the printer and the user selections"""
    stra = ''
    prototype = Prototype.objects.order_by('-date')[0]
    if str(prototype.surface) == 'Rough' :
        surf = np.float64(printer.layer_height_max)
        if str(printer.title) =='Connex 2':
            stra = 'High Speed'
    elif str(prototype.surface) == 'Smooth' :
        surf = np.float64(printer.layer_height_min)
        if str(printer.title) =='Connex 2':
            stra = 'High Quality'
    else :
        if str(printer.title) == 'Dimension Elite' :
            surf = np.float64(printer.layer_height_min)
        elif str(printer.title) == 'ProJet 3510 P' or str(printer.title) == 'ProJet 3510 T':
            surf =''
        else :
            surf = (np.float64(printer.layer_height_max)+np.float64(printer.layer_height_min))/2
    return surf, stra

def infill_proto(printer):
    """Determines the best filling according to the printer and the user selections"""
    prototype = Prototype.objects.order_by('-date')[0]
    if str(prototype.filling_proto) == 'emp' : 
        dens = np.float64(printer.infill_dens_proto_emp)
    elif str(prototype.filling_proto) == 'med' : 
        dens = np.float64(printer.infill_dens_proto_med)
    elif str(prototype.filling_proto) == 'ful' : 
        dens = np.float64(printer.infill_dens_proto_ful)
    return dens/100

def infill_proto_label(printer):
    """Determines the label of prototype filling according to the printer"""
    prototype = Prototype.objects.order_by('-date')[0]
    if str(prototype.filling_proto) == 'emp' : 
        label = str(printer.infill_dens_proto_emp_label)
    elif str(prototype.filling_proto) == 'med' : 
        label = str(printer.infill_dens_proto_med_label)
    elif str(prototype.filling_proto) == 'ful' : 
        label = str(printer.infill_dens_proto_ful_label)
    return label

def pattern_proto_label(printer):
    """Determines the label of prototype patern filling according to the printer"""
    prototype = Prototype.objects.order_by('-date')[0]
    pattern=''
    if prototype.use and (printer.infill_patt_proto_visu or printer.infill_patt_proto_func):
        if str(prototype.use) == 'Visual aid' or str(prototype.use) == 'Fit':
            pattern = str(printer.infill_patt_proto_visu)
        else :
            pattern = str(printer.infill_patt_proto_func)
    elif str(prototype.experience) == 'master' and (printer.infill_patt_proto_visu or printer.infill_patt_proto_func):
        if str(prototype.filling_proto) == 'emp' :
            pattern = str(printer.infill_patt_proto_visu)
        elif str(prototype.filling_proto) == 'med' or str(prototype.filling_proto) == 'ful' : 
            pattern = str(printer.infill_patt_proto_func)
        else : 
            pass
    else :
        pass
    return pattern 

def rotation(vector):
    """Determines the angle orientation of the stl file"""
    if (np.all(vector==[0,0,1]) == True) :
        lst_angle = [0,0,0]
    elif (np.all(vector==[0,0,-1]) == True) :
        lst_angle = [180,0,0]
    elif (np.all(vector==[0,1,0]) == True) :
        lst_angle = [90,0,0]
    elif (np.all(vector==[0,-1,0]) == True) :
        lst_angle = [-90,0,0]
    elif (np.all(vector==[1,0,0]) == True) :
        lst_angle = [0,90,0]
    elif (np.all(vector==[-1,0,0]) == True) :
        lst_angle = [0,-90,0]    
    return np.float64(lst_angle[0]), np.float64(lst_angle[1]), np.float64(lst_angle[2])

def common_calculations(alpha, file):

    name = os.path.splitext(os.path.basename(file))[0]
    obj = stl.Mesh.from_file(file)
    obj_bis = stl.Mesh.from_file(file)
    proj = plans_projection(obj)
    data_ele, lst_rack = val_elements(obj, proj)
    vol_stl = volume_stl(obj)/1000
    vol_boundingbox = volume_bounding_box(obj)/1000
    lst_vol_suppo_0, lst_vol_suppo_68 = list_volume_suppo(data_ele, alpha)

    vol_tot_support_0 = min(lst_vol_suppo_0)/1000
    index_vol_0 = lst_vol_suppo_0.index(min(lst_vol_suppo_0))
    rack_surf_0 = lst_rack[index_vol_0]/100

    vol_tot_support_68 = min(lst_vol_suppo_68)/1000
    index_vol_68 = lst_vol_suppo_68.index(min(lst_vol_suppo_68))
    rack_surf_68 = lst_rack[index_vol_68]/100

    lst_printers = choice_printers()

    vol_suppo_cost, price_cost, index_pri_cost, vol_real_cost, overhang_cost, vol_suppo_mate, price_mate, index_pri_mate, vol_real_mate, overhang_mate = optimisation(vol_stl, lst_printers, vol_tot_support_0, vol_tot_support_68, rack_surf_0, rack_surf_68)
    vector_0, plan_0 = proj[index_vol_0][0], proj[index_vol_0][1]
    vector_68, plan_68 = proj[index_vol_68][0], proj[index_vol_68][1]
    transform(obj, vector_0, plan_0, name, "0")
    transform(obj_bis, vector_68, plan_68, name, "68")
    return vol_boundingbox, plan_0, vector_0, plan_68, vector_68, name, vol_suppo_cost, price_cost, index_pri_cost, vol_real_cost, overhang_cost, vol_suppo_mate, price_mate, index_pri_mate, vol_real_mate, overhang_mate

def main_calculs() :
    prototype = Prototype.objects.order_by('-date')[0]
    file = prototype.file.path
    alpha = 45
    vol_bbox, plan_0, vector_0, plan_68, vector_68, name, vol_suppo_cost, price_cost, index_pri_cost, vol_real_cost, overhang_cost, vol_suppo_mate, price_mate, index_pri_mate, vol_real_mate, overhang_mate = common_calculations(alpha,str(file))
    result = Result(title = str(name))
    result.image_0.name = 'stl/' + name + '_0' + ".png"
    result.image_68.name = 'stl/' + name + '_68' + ".png"
    result.volume_prototype_mate = vol_real_mate
    result.volume_prototype_cost = vol_real_cost
    result.volume_boundingbox = vol_bbox
    result.volume_support_cost = vol_suppo_cost
    result.volume_support_mate = vol_suppo_mate
    result.price_cost = price_cost
    result.price_mate = price_mate
    printer_cost = Printer.objects.all()[index_pri_cost]
    printer_mate = Printer.objects.all()[index_pri_mate]
    result.layer_height_cost, result.strategy_cost = layer_height(printer_cost)
    result.layer_height_mate, result.strategy_mate = layer_height(printer_mate)
    result.volume_prototype_mate_label = infill_proto_label(printer_mate)
    result.volume_prototype_cost_label = infill_proto_label(printer_cost)
    result.material_cost = printer_cost.mate_proto
    result.material_mate = printer_mate.mate_proto
    result.printer_cost = printer_cost.title
    result.printer_mate = printer_mate.title
    result.pattern_proto_mate_label = pattern_proto_label(printer_mate)
    result.pattern_proto_cost_label = pattern_proto_label(printer_cost)
    result.pattern_support_cost = printer_cost.infill_label_suppo
    result.pattern_support_mate = printer_mate.infill_label_suppo
    result.overhang_cost = overhang_cost
    result.overhang_mate = overhang_mate
    result.rotation_0_X, result.rotation_0_Y, result.rotation_0_Z = rotation(vector_0)
    result.rotation_68_X, result.rotation_68_Y, result.rotation_68_Z = rotation(vector_68)
    result.save()

def calcul_level():
    level = Level.objects.order_by('-date')[0]
    sum_level = int(level.quest1)+int(level.quest2)+int(level.quest3)+int(level.quest4)
    return sum_level