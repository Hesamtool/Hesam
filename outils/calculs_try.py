
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
        fill_suppo = np.float64(printer.filling_proto)
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
    vector, plan= proj[index_vol][0], proj[index_vol][1]
    transform(obj, vector, plan, name)
    lst_printers = choice_printers()
    vol_suppo_cost, price_cost, index_pri_cost, vol_suppo_mate, price_mate, index_pri_mate = optimisation(vol_stl, vol_tot_support, lst_printers)
    
