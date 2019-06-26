# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:44:39 2019

@author: Utilisateur
"""
import math
import os
import stl
import matplotlib.pyplot as plt
import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from .models import Prototype, Material_proto, Material_support, Result, Printer, Level

# find the max dimensions, so we can know the bounding box, getting the height,
# width, length (because these are the step size)...
    
def find_mins_maxs(obj):
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

def plot_stl(obj, name) :
    """Plot of STL and Bounding box"""
    figure = plt.figure(facecolor="white")
    axes = mplot3d.Axes3D(figure)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(obj.vectors, facecolors='green', linewidths = 1)) #Plot the STL part
    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(obj) #Plot the bounding box
    xs = [minx, minx, minx, minx, maxx, maxx, maxx, maxx]
    ys = [miny, miny, maxy, maxy, miny, miny, maxy, maxy]
    zs = [minz, maxz, minz, maxz, minz, maxz, minz, maxz]
    axes.scatter(xs, ys, zs, c='green')
    axes.set_xticklabels([])
    axes.set_yticklabels([])
    axes.set_zticklabels([])
    scale = obj.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    plt.savefig("media/stl/" + str(name) + ".png", transparent = True)

def volume_bounding_box(obj) : 
    """Calculation the volume of the bounding box"""
    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(obj)
    Vol = (maxx-minx)*(maxy-miny)*(maxz-minz)
    return Vol

def volume_stl(obj) :
    """Calculation the volume of the STL part"""
    prototype = Prototype.objects.order_by('-date')[0]
    if prototype.filling_proto :
        fill_proto = np.float64(prototype.filling_proto)
    else :
        fill_proto = 0.5
    volume, cog, inertia = obj.get_mass_properties()
    return volume * fill_proto
        
def val_elements(obj, proj) : 
    """Calculation of the support volume for each triangle according to the projection plane without the filling"""
    normales = []
    triangles = obj.vectors
    plans = proj
    normales = normal_vectors(obj)
    data_ele = []
    for support in plans :
        elements = []
        for n, triangle in enumerate(triangles) :
            lmoy = 0
            pro_pts = []
            angle = np.degrees(np.arccos(np.dot(support[0], normales[n])/(np.linalg.norm(support[0])*np.linalg.norm(normales[n]))))
            for point in triangle :
                pro_pts.append(point - (np.vdot(support[0], point)-np.vdot(support[0], support[1]))/np.vdot(support[0], support[0])*support[0])    # Projection des points
                lmoy += np.linalg.norm(point-pro_pts[-1])/3     # Longueur moyenne
            if angle <= 90 :
                vol_ele = -lmoy * np.linalg.norm(np.cross(pro_pts[0]-pro_pts[1], pro_pts[2]-pro_pts[1]))/2
            else :
                vol_ele = +lmoy * np.linalg.norm(np.cross(pro_pts[0]-pro_pts[1], pro_pts[2]-pro_pts[1]))/2
            elements.append([pro_pts, vol_ele, angle])
        data_ele.append(elements)
    return data_ele   
        
def normal_vectors(obj) :
    """Calculation of the normal vectors"""
    normals = []
    triangles = obj.vectors
    for triangle in triangles :
        vec = np.cross(triangle[1]-triangle[0], triangle[2]-triangle[0])
        normals.append(vec/np.linalg.norm(vec))
    return normals
        
def liste_volume_suppo(data_ele, alpha):
    """Sum of the volume support of each triangle according to the angle alpha without the filling"""
    lst_vol_sup = []
    for support in data_ele :
        volume = 0
        for element in support :
            if element[2] >= (alpha+90):
                volume += element[1]
        lst_vol_sup.append(volume)
    return lst_vol_sup
         
def plan_projection(obj):
    """Select projection plans"""
    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(obj)
    proj = np.array([[[0,0,1],[0,0,minz]],[[0,0,-1],[0,0,maxz]],[[0,1,0],[0,miny,0]],[[0,-1,0],[0,maxy,0]],[[1,0,0],[minx,0,0]],[[-1,0,0],[maxx,0,0]]])
    return proj

def transform(obj, vector, plan, name):
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
    plot_stl(obj, name)
    
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
        and (not prototype.colour or prototype.colour == str(printer.colour)) \
        and (not prototype.thermal_resistance or prototype.thermal_resistance == str(printer.thermal_resistance)) \
        and (not prototype.optical_resistance or prototype.optical_resistance == str(printer.optical_resistance)) \
        and (not prototype.printing_speed or prototype.printing_speed == str(printer.printing_speed)) \
        and (not str(printer.mate_proto) in lst_material_no[0]) \
        and (not str(printer.technology) in lst_technology_no[0]):
            lst_printer.append(pri)
    return lst_printer


def optimisation (vol_stl, vol_tot_support, lst_printers) :
    price_cost = 0
    index_pri_cost = 0
    vol_sup_cost = 0
    price_mate = 0
    index_pri_mate = 0
    vol_sup_mate = 0
    for pri in lst_printers:
        printer = Printer.objects.all()[pri]
        price_suppo = np.float64(Material_support.objects.get(title = printer.mate_suppo).price)
        price_proto = np.float64(Material_proto.objects.get(title = printer.mate_proto).price)
        dens_suppo = np.float64(Material_support.objects.get(title = printer.mate_suppo).density)
        dens_proto = np.float64(Material_proto.objects.get(title = printer.mate_proto).density)
        lost_suppo = np.float64(printer.qtt_material_suppo_lost)
        lost_proto = np.float64(printer.qtt_material_proto_lost)
        fill_suppo = np.float64(printer.fill_suppo)
        vol_support = vol_tot_support * fill_suppo
        price = (vol_stl + lost_proto) * price_proto * dens_proto + (vol_support + lost_proto) * dens_suppo * price_suppo
        if price_cost == 0 or price_mate == 0 :
            price_mate = price
            price_cost = price
            index_pri_cost = pri
            index_pri_mate = pri
            vol_sup_cost = vol_support
            vol_sup_mate = vol_support
        else :
            # Optimisation of cost
            if price < price_cost :
                price_cost = price
                index_pri_cost = pri
                vol_sup_cost = vol_support
            elif price == price_cost and vol_support < vol_sup_cost :
                price_cost = price
                index_pri_cost = pri
                vol_sup_cost = vol_support
            # Optimisation of material
            if vol_support < vol_sup_mate :
                price_mate = price
                index_pri_mate = pri
                vol_sup_mate = vol_support
            elif vol_support == vol_sup_mate and price < price_mate :
                price_mate = price
                index_pri_mate = pri
                vol_sup_mate = vol_support
    return round(vol_sup_cost,0), round(price_cost,2), index_pri_cost, round(vol_sup_mate,0), round(price_mate,2), index_pri_mate

def common_calculations(alpha, file) :

    name = os.path.splitext(os.path.basename(file))[0]
    obj = mesh.Mesh.from_file(file)
    proj = plan_projection(obj)
    data_ele = val_elements(obj, proj)
    vol_stl = volume_stl(obj)
    vol_boundingbox = volume_bounding_box(obj)
    lst_vol_suppo = liste_volume_suppo(data_ele, alpha)
    vol_tot_support = min(lst_vol_suppo)
    index_vol = lst_vol_suppo.index(vol_tot_support)
    vector, plan = proj[index_vol][0], proj[index_vol][1]
    transform(obj, vector, plan, name)
    lst_printers = choice_printers()
    vol_suppo_cost, price_cost, index_pri_cost, vol_suppo_mate, price_mate, index_pri_mate = optimisation(vol_stl, vol_tot_support, lst_printers)
    return (vol_stl/1000), vol_boundingbox/1000, plan, vector, name, vol_suppo_cost/1000, price_cost, index_pri_cost, vol_suppo_mate/1000, price_mate, index_pri_mate

def main_calculs() :
    prototype = Prototype.objects.order_by('-date')[0]
    file = prototype.file.path
    alpha = 45
    vol_stl, vol_bbox, plan, vector, name, vol_suppo_cost, price_cost, index_pri_cost, vol_suppo_mate, price_mate, index_pri_mate = common_calculations(alpha,str(file))
    result = Result(title = str(name))
    result.image.name = 'stl/' + name + ".png"
    result.volume_prototype = vol_stl
    result.volume_boundingbox = vol_bbox
    result.volume_support_cost = vol_suppo_cost
    result.volume_support_mate = vol_suppo_mate
    result.price_cost = price_cost
    result.price_mate = price_mate
    printer_cost = Printer.objects.all()[index_pri_cost]
    printer_mate = Printer.objects.all()[index_pri_mate]
    result.material_cost = printer_cost.mate_proto
    result.material_mate = printer_mate.mate_proto
    result.printer_cost = printer_cost.title
    result.printer_mate = printer_mate.title
    result.save()

def calcul_level():
    level = Level.objects.order_by('-date')[0]
    sum_level = int(level.quest1)+int(level.quest2)+int(level.quest3)+int(level.quest4)
    return sum_level