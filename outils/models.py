from django.db import models
from django.utils import timezone

class Level(models.Model):
    date = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = "Hours of level")
    quest1 = models.IntegerField()
    quest2 = models.IntegerField()
    quest3 = models.IntegerField()
    quest4 = models.IntegerField()

    class Meta:
        verbose_name = "Level"

    def __str__(self):
        return self.date

class Use(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Use"
    
    def __str__(self):
        return self.title


class Sector(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Sector"
    
    def __str__(self):
        return self.title


class Material_proto(models.Model):
    title = models.CharField(max_length = 100)
    density = models.FloatField(blank = True, null = True)
    temperature_fusion = models.IntegerField(blank = True, null = True)
    price = models.FloatField(blank = True, null = True)

    class Meta:
        verbose_name = "Material proto"
    
    def __str__(self):
        return self.title


class Material_support(models.Model):
    title = models.CharField(max_length = 100)
    density = models.FloatField(blank = True, null = True)
    temperature_fusion = models.IntegerField(blank = True, null = True)
    price = models.FloatField(blank = True, null = True)

    class Meta:
        verbose_name = "Material support"
    
    def __str__(self):
        return self.title


class Technology(models.Model):
    title = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "Technology"

    def __str__(self):
        return self.title

class Prototype(models.Model):
    experience= models.CharField(max_length = 100)
    use = models.ForeignKey('Use', on_delete = models.CASCADE, blank = True, null = True)
    sector = models.ForeignKey('Sector', on_delete = models.CASCADE, blank = True, null = True)
    date = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = "Date de prototypage")
    file = models.FileField(upload_to ='stl/',verbose_name = "STL", null = True, blank = True)
    colour = models.CharField(max_length = 100, blank = True)
    material_yes = models.ManyToManyField(Material_proto, related_name = "Material_proto_yes", blank = True)
    material_no = models.ManyToManyField(Material_proto, related_name = "Material_proto_no", blank = True)
    surface = models.CharField(max_length = 100, blank = True, null = True)
    filling_proto = models.CharField(max_length = 100, blank = True, null = True)
    thermal_resistance = models.CharField(max_length = 100, blank = True, null = True)
    optical_resistance = models.CharField(max_length = 100, blank = True, null = True)
    printing_speed = models.CharField(max_length = 100, blank = True, null = True)
    technology_yes = models.ManyToManyField(Technology, related_name = "technology_yes", blank = True)
    technology_no = models.ManyToManyField(Technology, related_name = "Technology_no", blank = True)

    def get_material_yes(self):
        return"\n".join([p.title for p in self.material_yes.all()])

    def get_material_no(self):
        return"\n".join([p.title for p in self.material_no.all()])

    def get_technology_yes(self):
        return"\n".join([p.title for p in self.technology_yes.all()])

    def get_technology_no(self):
        return"\n".join([p.title for p in self.technology_no.all()])


    class Meta:
        verbose_name = "Prototype"

    def __str__(self):
        return str(self.use)

class Infill_Pattern_Prototype_Visual (models.Model) :
    title = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "Pattern Prototype Visual"

    def __str__(self):
        return str(self.title)


class Infill_Pattern_Prototype_Functionnal (models.Model) :
    title = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "Pattern Prototype Functionnal"

    def __str__(self):
        return str(self.title)

class Printer(models.Model):
    title = models.CharField(max_length = 100)
    technology = models.ForeignKey('Technology', on_delete = models.CASCADE, blank = True, null = True)
    mate_suppo = models.ForeignKey('Material_support', on_delete = models.CASCADE)
    mate_proto = models.ForeignKey('Material_proto', on_delete = models.CASCADE, blank = True, null = True)
    qtt_material_proto_lost = models.IntegerField(blank = True, null = True)
    qtt_material_suppo_lost = models.IntegerField(blank = True, null = True)
    colour = models.ForeignKey('Colour', on_delete = models.CASCADE, blank = True, null = True)
    thermal_resistance = models.ForeignKey('Thermal_resistance', on_delete = models.CASCADE, blank = True, null = True)
    optical_resistance = models.ForeignKey('Optical_resistance', on_delete = models.CASCADE, blank = True, null = True)
    printing_speed = models.ForeignKey('Printing_speed', on_delete = models.CASCADE, blank = True, null = True)
    infill_dens_proto_emp = models.FloatField(blank = True, null = True)
    infill_dens_proto_med = models.FloatField(blank = True, null = True)
    infill_dens_proto_ful = models.FloatField(blank = True, null = True)
    infill_dens_proto_emp_label = models.CharField(max_length = 100, blank = True, null = True)
    infill_dens_proto_med_label = models.CharField(max_length = 100, blank = True, null = True)
    infill_dens_proto_ful_label = models.CharField(max_length = 100, blank = True, null = True)
    infill_dens_suppo = models.FloatField(blank = True, null = True)
    infill_label_suppo = models.CharField(max_length = 100, blank = True, null = True)
    infill_patt_proto_visu = models.ForeignKey('Infill_Pattern_Prototype_Visual', on_delete = models.CASCADE, blank = True, null = True)
    infill_patt_proto_func = models.ForeignKey('Infill_Pattern_Prototype_Functionnal', on_delete = models.CASCADE, blank = True, null = True)
    layer_height_min = models.FloatField(blank = True, null = True)
    layer_height_max = models.FloatField(blank = True, null = True)

    class Meta:
        verbose_name = "Printer"

    def __str__(self):
        return str(self.title)


class Colour(models.Model):
    title = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "Colour"

    def __str__(self):
        return str(self.title)


class Thermal_resistance(models.Model):
    title = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "Thermal resistance"

    def __str__(self):
        return str(self.title)


class Optical_resistance(models.Model):
    title = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "Optical resistance"

    def __str__(self):
        return str(self.title)

class Printing_speed(models.Model):
    title = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "Printing speed"

    def __str__(self):
        return str(self.title)


class Result(models.Model):
    date = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = "Date des calculs")
    title = models.CharField(max_length = 100)
    price_cost = models.FloatField(blank = True, null = True)
    price_mate = models.FloatField(blank = True, null = True)
    volume_prototype_cost = models.FloatField(blank = True, null = True)
    volume_prototype_mate = models.FloatField(blank = True, null = True)
    volume_prototype_cost_label = models.CharField(max_length = 100, blank = True, null = True)
    volume_prototype_mate_label = models.CharField(max_length = 100, blank = True, null = True)
    volume_boundingbox = models.FloatField(blank = True, null = True)
    volume_support_cost = models.FloatField(blank = True, null = True)
    volume_support_mate = models.FloatField(blank = True, null = True)
    layer_height_cost = models.FloatField(blank = True, null = True)
    layer_height_mate = models.FloatField(blank = True, null = True)
    material_cost = models.CharField(max_length = 100, blank = True, null = True)
    material_mate = models.CharField(max_length = 100, blank = True, null = True)
    printer_cost = models.CharField(max_length = 100, blank = True, null = True)
    printer_mate = models.CharField(max_length = 100, blank = True, null = True)
    pattern_support_cost = models.CharField(max_length = 100, blank = True, null = True)
    pattern_support_mate = models.CharField(max_length = 100, blank = True, null = True)
    pattern_proto_mate_label = models.CharField(max_length = 100, blank = True, null = True)
    pattern_proto_cost_label = models.CharField(max_length = 100, blank = True, null = True)
    dens_proto_cost = models.CharField(max_length = 100, blank = True, null = True)
    dens_proto_mate = models.CharField(max_length = 100, blank = True, null = True)
    image = models.ImageField(blank = True, null = True)
    rotation_X = models.FloatField(blank = True, null = True)
    rotation_Y = models.FloatField(blank = True, null = True)
    rotation_Z = models.FloatField(blank = True, null = True)

    class Meta:
        verbose_name = "Result"

    def __str__(self):
        return str(self.title)