from django.contrib import admin
from .models import Use, Sector, Prototype, Material_proto, Material_support, Printer, Technology, Result, Colour, Thermal_resistance, Optical_resistance, Printing_speed, Level, Infill_Pattern_Prototype_Functionnal, Infill_Pattern_Prototype_Visual
class PrototypeAdmin(admin.ModelAdmin):
	list_display = ('use', 'sector', 'date', 'file', 'colour', 'get_material_yes', 'get_material_no', 'surface', 'experience', 'filling_proto', 'thermal_resistance','optical_resistance', 'printing_speed', 'get_technology_yes','get_technology_no')
	list_filter = ('use','sector',)
	date_hierarchy = 'date'
	ordering = ('date', )
	search_fields = ('use', 'sector')

class Material_protoAdmin(admin.ModelAdmin):
	list_display = ('title','density','temperature_fusion','price')
	list_filter = ('title','density','temperature_fusion','price',)
	ordering = ('title',)

class Material_supportAdmin(admin.ModelAdmin):
	list_display = ('title','density','temperature_fusion','price')
	list_filter = ('title','density','temperature_fusion','price',)
	ordering = ('title',)

class ResultAdmin(admin.ModelAdmin):
	list_display = ('date','title', 'price_cost','price_mate','volume_prototype_mate_label', 'volume_prototype_cost_label','volume_boundingbox','volume_support_cost','volume_support_mate','image')
	list_filter = ('date','title', 'price_cost','price_mate','volume_prototype_mate_label', 'volume_prototype_cost_label','volume_boundingbox','volume_support_cost','volume_support_mate','image',)
	ordering = ('date',)

class LevelAdmin(admin.ModelAdmin):
	list_display = ('date','quest1','quest2','quest3','quest4')
	list_filter = ('date','quest1','quest2','quest3','quest4',)
	ordering = ('date',)

admin.site.register(Level, LevelAdmin)
admin.site.register(Use)
admin.site.register(Sector)
admin.site.register(Prototype, PrototypeAdmin)
admin.site.register(Material_proto, Material_protoAdmin)
admin.site.register(Material_support, Material_supportAdmin)
admin.site.register(Printer)
admin.site.register(Technology)
admin.site.register(Result, ResultAdmin)
admin.site.register(Colour)
admin.site.register(Thermal_resistance)
admin.site.register(Optical_resistance)
admin.site.register(Printing_speed)
admin.site.register(Infill_Pattern_Prototype_Visual)
admin.site.register(Infill_Pattern_Prototype_Functionnal)