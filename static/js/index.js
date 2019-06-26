/*Sectors colour change */

var in_sect=[0,0,0,0,0,0];
var lst_sect=['medi','aero','auto','luxu','oil','othe'];
var sha_ina = "0 9px grey";
var sha_ac = "0 9px green";
var ac = 'grid';
var ina = 'none';
var sta_uses = [[ac, ina, ina, ac],[ina, ina, ac, ac],[ina, ina, ac, ac],[ac, ac, ina, ina],[ina, ina, ac, ac],[ac, ac, ac, ac]];
var lst_sel_uses = ['ergo_all', 'esth_all', 'asse_all', 'func_all']
var lst_img_sect = ['img_medi_ina','img_medi_ac','img_aero_ina','img_aero_ac','img_auto_ina','img_auto_ac','img_luxu_ina','img_luxu_ac','img_oil_ina','img_oil_ac','img_othe_ina','img_othe_ac']
var lst_img_use = ['img_medi_use','img_aero_use','img_auto_use','img_luxu_use','img_oil_use','img_othe_use'];
function change_sector(sector)
{
for (var i=0; i<lst_img_use.length; i++)
	{
	img_use_beg = document.getElementsByClassName(lst_img_use[i]);
	for (var j=0; j<img_use_beg.length; j++)
		{
		img_use_beg[j].style.display = 'none';
		}
	}
for (var k=0; k<lst_sect.length; k++)
	{
	if (lst_sect[k]==sector)
		{
		lst_sta_sect= ['inline-block', 'none', 'inline-block', 'none','inline-block', 'none', 'inline-block', 'none','inline-block', 'none', 'inline-block', 'none','inline-block', 'none'];
		shadow = [sha_ina,sha_ina,sha_ina,sha_ina,sha_ina,sha_ina];
		checked=[false,false,false,false,false,false];		
		if (in_sect[k]==0)
			{
			in_sect=[0,0,0,0,0,0];
			in_sect[k]=1;
			shadow[k]=sha_ac;
			checked[k]=true;
			state = sta_uses[k]
			lst_sta_sect[2*k]='none';
			lst_sta_sect[(2*k)+1]='inline-block';
			img_use = document.getElementsByClassName(lst_img_use[k]);
			}
		else
			{
			in_sectors=[0,0,0,0,0,0];
			img_use = document.getElementsByClassName(lst_img_use[5]);
			}
		}
	}
for (var m=0; m<lst_sect.length; m++)
	{
		document.getElementById(lst_sect[m]).checked = checked[m];
		document.getElementById(lst_img_sect[2*m]).style.boxShadow = shadow[m];
		document.getElementById(lst_img_sect[(2*m)+1]).style.boxShadow = shadow[m];
		document.getElementById(lst_img_sect[2*m]).style.display = lst_sta_sect[2*m];
		document.getElementById(lst_img_sect[(2*m)+1]).style.display = lst_sta_sect[(2*m)+1];
	}
for (var n=0; n<lst_sel_uses.length; n++)
	{
	document.getElementById(lst_sel_uses[n]).style.display = state[n];
	}
for (var p=0; p<img_use.length; p++)
	{
	img_use[p].style.display = 'inline-block';
	}
}

/*Uses colour change*/

var in_uses=[0,0,0,0];
var lst_uses=['ergo','esth','asse','func'];
var sha_ina = "0 9px grey";
var sha_ac = "0 9px green";
var lst_img_uses = ['img_ergo_ina','img_ergo_ac','img_esth_ina','img_esth_ac','img_asse_ina','img_asse_ac','img_func_ina','img_func_ac']
var z_use=0;
function change_use(use)
{
for (var k=0; k<lst_uses.length; k++)
	{
	if (lst_uses[k] == use)
		{
		lst_sta_uses = ['inline-block','none','inline-block','none','inline-block','none','inline-block','none'];
		shadow = [sha_ina,sha_ina,sha_ina,sha_ina];	
		checked = [false,false,false,false];
		z_use = 1;	
		if (in_uses[k]==0)
			{
			in_uses=[0,0,0,0];
			in_uses[k]=1;
			shadow[k]=sha_ac;
			checked[k]=true;
			lst_sta_uses[2*k]='none';
			lst_sta_uses[(2*k)+1]='inline-block';
			}
		else
			{
			in_uses = [0,0,0,0];
			}
		}
	}
if (z_use == 0)
{
	lst_sta_uses=['inline-block','none','inline-block','none','inline-block','none','inline-block','none'];
	shadow = [sha_ina,sha_ina,sha_ina,sha_ina];	
	checked=[false,false,false,false];
	in_uses=[0,0,0,0];
}
z_use=0;
for (var m=0; m<lst_uses.length; m++)
	{
		document.getElementById(lst_uses[m]).checked = checked[m];
		document.getElementById(lst_img_uses[2*m]).style.boxShadow = shadow[m];
		document.getElementById(lst_img_uses[(2*m)+1]).style.boxShadow = shadow[m];
		document.getElementById(lst_img_uses[2*m]).style.display = lst_sta_uses[2*m];
		document.getElementById(lst_img_uses[(2*m)+1]).style.display = lst_sta_uses[(2*m)+1];
	}
}

/*Criteria coulour change*/

var lst_crit = ['tec', 'mat', 'sur', 'fil', 'col', 'the', 'opt', 'spe'];
var cri_ina = 'rgb(178,178,178)';
var cri_ac = 'rgba(170,30,120,1)';
var cri_done = 'rgba(135,25,96,1)';
var lst_id_crit = ['cri_tech','cri_mate','cri_surf','cri_fill','cri_colo','cri_ther','cri_opti','cri_spee'];
var lst_ong_crit = ['ong_tec','ong_mat','ong_sur','ong_fil','ong_col','ong_the','ong_opt','ong_spe'];


function switch_cri(onglet)
{
for (var k=0; k<lst_crit.length; k++)
	{
	if (onglet==lst_crit[k])
		{
		var colour_cri = [cri_ina,cri_ina,cri_ina,cri_ina,cri_ina,cri_ina,cri_ina,cri_ina,cri_ina]
		var val_cri = ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none'];
		val_cri[k] ='grid';
		if(k==0)
			{
			colour_cri = [cri_ac,cri_ina,cri_ina,cri_ina,cri_ina,cri_ina,cri_ina,cri_ina,cri_ina];
			}
		if(k>0)
			{	
			for(var l=0; l<k; l++)
				{	
				colour_cri[l]=cri_done;
				}
			}
		colour_cri[k] = cri_ac;
		}
	}
for (var m=0; m<lst_crit.length; m++)
	{
		document.getElementById(lst_id_crit[m]).style.display = val_cri[m]
		document.getElementById(lst_ong_crit[m]).style.backgroundColor = colour_cri[m]
	}
}

/*Change colors colors*/

var col_ina = "grey";
var col_ac = "green";
var in_colours=[0,0,0];
var lst_colours=['tran','mono','mult'];
var z_colo=0;

function change_colour_colo(colour)
{
for (var k=0; k<lst_colours.length; k++)
	{
	if (lst_colours[k]==colour)
		{
		z_colo=1;
		colours=[col_ina,col_ina,col_ina];
		checked=[false,false,false];		
		if (in_colours[k]==0)
			{
			in_colours=[0,0,0];
			in_colours[k]=1;
			colours[k]=col_ac;
			checked[k]=true;
			}
		else
			{
			in_colours=[0,0,0];
			}
		}
	}
if (z_colo==0)
	{
	colours=[col_ina,col_ina,col_ina];
	checked=[false,false,false];
	in_colours=[0,0,0];
	}
z_colo=0;
label_tran.style.backgroundColor = colours[0];
label_mono.style.backgroundColor = colours[1];
label_mult.style.backgroundColor = colours[2];
document.getElementById("tran").checked = checked[0];
document.getElementById("mono").checked = checked[1];
document.getElementById("mult").checked = checked[2];
}

/*Materials coulour change*/

var mate_ina = "grey";
var mate_ac_yes = "green";
var mate_ac_no = "red";
var colours_mate=[mate_ina,mate_ina,mate_ina,mate_ina];
var in_materials=[0,0,0,0];
var lst_materials=['mate_1','mate_2','mate_3','mate_4'];
var checked_yes_mate = [false,false,false,false];
var checked_no_mate = [false,false,false,false];
var z_mate = 0;

function change_material(material)
{
for (var k=0; k<lst_materials.length; k++)
	{
	if (lst_materials[k]==material)
		{
		z_mate = 1;		
		if (in_materials[k]==0)
			{
			in_materials[k]=1;
			colours_mate[k]=mate_ac_yes;
			checked_yes_mate[k]=true;
			checked_no_mate[k]=false;
			}
		else if (in_materials[k]==1)
			{
			in_materials[k]=2;
			colours_mate[k]=mate_ac_no;
			checked_yes_mate[k]=false;
			checked_no_mate[k]=true;
			}
		else
			{
			in_materials[k]=0;
			colours_mate[k]=mate_ina;
			checked_yes_mate[k]=false;
			checked_no_mate[k]=false;
			}
		}
	}
if (z_mate == 0)
	{	
	colours=[mate_ina,mate_ina,mate_ina,mate_ina];
	checked_yes = [false,false,false,false];
	checked_no = [false,false,false,false];
	in_materials=[0,0,0,0];
	}
z_mate=0;

label_mate_1.style.backgroundColor = colours_mate[0];
label_mate_2.style.backgroundColor = colours_mate[1];
label_mate_3.style.backgroundColor = colours_mate[2];
label_mate_4.style.backgroundColor = colours_mate[3];
document.getElementById("mate_1").checked = checked_yes_mate[0];
document.getElementById("mate_2").checked = checked_yes_mate[1];
document.getElementById("mate_3").checked = checked_yes_mate[2];
document.getElementById("mate_4").checked = checked_yes_mate[3];
document.getElementById("mate_1_no").checked = checked_no_mate[0];
document.getElementById("mate_2_no").checked = checked_no_mate[1];
document.getElementById("mate_3_no").checked = checked_no_mate[2];
document.getElementById("mate_4_no").checked = checked_no_mate[3];
}

/*Finish surface colour change*/

var in_surfaces=[0,0,0];
var lst_surfaces=['fair','aver','good'];
var sha_ina = "0 9px grey";
var sha_ac = "0 9px green";
var z_surf = 0;
function change_surface(surface)
{
for (var k=0; k<lst_surfaces.length; k++)
	{
	if (lst_surfaces[k]==surface)
		{
		z_surf=1;
		checked=[false,false,false];
		shadow = [sha_ina,sha_ina,sha_ina];		
		if (in_surfaces[k]==0)
			{
			in_surfaces=[0,0,0];
			in_surfaces[k]=1;
			checked[k]=true;
			shadow[k]= sha_ac;
			}
		else
			{
			in_surfaces=[0,0,0];
			}
		}
	}
if (z_surf==0)
	{	
	checked=[false,false,false];
	shadow = [sha_ina,sha_ina,sha_ina];
	in_surfaces=[0,0,0];	
	}
z_surf = 1;
document.getElementById("fair").checked = checked[0];
document.getElementById("aver").checked = checked[1];
document.getElementById("good").checked = checked[2];
document.getElementById("img_fair").style.boxShadow = shadow[0];
document.getElementById("img_aver").style.boxShadow = shadow[1];
document.getElementById("img_good").style.boxShadow = shadow[2];
}

/*Filling change colors*/

var in_fill=[0,0,0];
var lst_fill=['emp','med','ful'];
var sha_ina = "0 9px grey";
var sha_ac = "0 9px green";
var z_fill = 0;
function change_colour_filling(fill)
{
for (var k=0; k<lst_fill.length; k++)
	{
	if (lst_fill[k]==fill)
		{
		z_fill = 1;
		checked=[false,false,false];
		shadow=[sha_ina,sha_ina,sha_ina];
		if (in_fill[k]==0)
			{
			in_fill=[0,0,0];
			in_fill[k]=1;
			shadow[k]=sha_ac;
			checked[k]=true;
			}
		else
			{
			in_fill=[0,0,0];
			}
		}
	}
if (z_fill == 0)
	{
	checked = [false,false,false];
	shadow = [sha_ina,sha_ina,sha_ina];
	in_fill=[0,0,0];
	}
z_fill=0;

document.getElementById("emp").checked = checked[0];
document.getElementById("med").checked = checked[1];
document.getElementById("ful").checked = checked[2];
document.getElementById("img_emp").style.boxShadow = shadow[0];
document.getElementById("img_med").style.boxShadow = shadow[1];
document.getElementById("img_ful").style.boxShadow = shadow[2];
}

/*Colours change of thermal resistances*/

var the_ina = "grey";
var the_ac = "green";
var thermals=[the_ina,the_ina];
var in_thermals=[0,0];
var lst_thermals=['yes','no'];
var z_ther = 0;

function change_colour_ther(colour)
{
for (var k=0; k<lst_thermals.length; k++)
	{
	if (lst_thermals[k]==colour)
		{
		z_ther = 1;
		thermals=[the_ina,the_ina];
		checked=[false,false];		
		if (in_thermals[k]==0)
			{
			in_thermals=[0,0];
			in_thermals[k]=1;
			thermals[k]=the_ac;
			checked[k]=true;
			}
		else
			{
			in_thermals=[0,0];
			}
		}
	}
if (z_ther == 0)
	{	
	thermals=[the_ina,the_ina];
	checked=[false,false];
	in_thermals=[0,0];	
	}
z_ther = 0;
label_yes_ther.style.backgroundColor = thermals[0];
label_no_ther.style.backgroundColor = thermals[1];
document.getElementById("yes_ther").checked = checked[0];
}

/*Colours change of environnement resistances*/

var env_ina = "grey";
var env_ac = "green";
var opticals=[env_ina,env_ina];
var in_opticals=[0,0];
var lst_opticals=['yes','no'];
var z_opti = 0;

function change_colour_opti(colour)
{
for (var k=0; k<lst_opticals.length; k++)
	{
	if (lst_opticals[k]==colour)
		{
		opticals=[env_ina,env_ina];
		checked=[false,false];	
		z_opti = 1;	
		if (in_opticals[k]==0)
			{
			in_opticals=[0,0];
			in_opticals[k]=1;
			opticals[k]=env_ac;
			checked[k]=true;
			}
		else
			{
			in_opticals=[0,0];
			}
		}
	}
if (z_opti==0)
	{
	opticals=[env_ina,env_ina];
	checked=[false,false];
	in_opticals=[0,0];	
	}
z_opti = 0;
label_yes_opti.style.backgroundColor = opticals[0];
label_no_opti.style.backgroundColor = opticals[1];
document.getElementById("yes_opti").checked = checked[0];
}

/*Colours change of printing speeds */
var pri_ina = "grey";
var pri_ac = "green";
var speeds=[pri_ina,pri_ina];
var in_speeds=[0,0];
var lst_speeds=['yes','no'];
var z_spee = 0;

function change_colour_spee(colour)
{
for (var k=0; k<lst_speeds.length; k++)
	{
	if (lst_speeds[k]==colour)
		{
		z_spee = 1;
		speeds=[pri_ina,pri_ina];
		checked=[false,false];		
		if (in_speeds[k]==0)
			{
			in_speeds=[0,0];
			in_speeds[k]=1;
			speeds[k]=pri_ac;
			checked[k]=true;
			}
		else
			{
			in_speeds=[0,0];
			}
		}
	}
if (z_spee == 0)
	{
	speeds=[pri_ina,pri_ina];
	checked=[false,false];
	in_speeds=[0,0];	
	}
z_spee = 0;
label_yes_spee.style.backgroundColor = speeds[0];
label_no_spee.style.backgroundColor = speeds[1];
document.getElementById("yes_spee").checked = checked[0];
}

/*Colours change of technologies*/

var in_tech = [0,0,0,0,0,0,0];
var lst_tech_yes = ['tec1','tec2','tec3','tec4','tec5','tec6','tec7'];
var lst_tech_no = ['tec1_no','tec2_no','tec3_no','tec4_no','tec5_no','tec6_no','tec7_no'];
var lst_img_tech = ['img_tec1','img_tec2','img_tec3','img_tec4','img_tec5','img_tec6','img_tec7']
var sha_ina = "0 9px grey";
var sha_ac = "0 9px green";
var sha_ac_no = "0 9px red";
var shadow_tech = [sha_ina,sha_ina,sha_ina,sha_ina,sha_ina,sha_ina,sha_ina];
var checked_yes_tech = [false,false,false,false,false,false,false,false];
var checked_no_tech = [false,false,false,false,false,false,false,false];
var z_tech = 0;

function change_technology(techno)
{
for (var k=0; k<lst_tech_yes.length; k++)
	{
	if (lst_tech_yes[k]==techno)
		{
		z_tech = 1;
		if (in_tech[k]==2)
			{
			in_tech[k]=0;
			checked_yes_tech[k]=false;
			checked_no_tech[k]=false;
			shadow_tech[k]= sha_ina;
			}
		else if (in_tech[k]==1)
			{
			in_tech[k]=2;
			checked_yes_tech[k]=false;
			checked_no_tech[k]=true;
			shadow_tech[k]= sha_ac_no;
			}
		else if (in_tech[k]==0)
			{
			in_tech[k]=1;
			checked_yes_tech[k]=true;
			checked_no_tech[k]=false;
			shadow_tech[k]= sha_ac;
			}
		}
	}
if (z_tech == 0)
	{
	shadow_tech = [sha_ina,sha_ina,sha_ina,sha_ina,sha_ina,sha_ina,sha_ina];
	checked_yes_tech = [false,false,false,false,false,false,false,false];
	checked_no_tech = [false,false,false,false,false,false,false,false];
	in_tech = [0,0,0,0,0,0,0];
	}
z_tech = 0;
for (var m=0; m<lst_tech_yes.length; m++)
	{
		document.getElementById(lst_tech_yes[m]).checked = checked_yes_tech[m];
		document.getElementById(lst_tech_no[m]).checked = checked_no_tech[m];
		document.getElementById(lst_img_tech[m]).style.boxShadow = shadow_tech[m];
	}
}

/*Sheet change of beginner*/

var lst_beg = ['sec', 'use', 'cri', 'stl'];
var ina = 'rgba(120,120,120,1)';
var ac = 'rgba(170,30,120,1)';
var done = 'rgba(135,25,96,1)';
var lst_colour_beg = [[ac,ina,ina,ina],[done,ac,ina,ina],[done,done,ac,ina],[done,done,done,ac]]

function switch_beg(onglet)
{
for (var k=0; k<lst_beg.length; k++)
	{
	if (onglet==lst_beg[k])
		{
		var val_beg = ['none', 'none', 'none', 'none'];
		val_beg[k] ='grid';
		colour_beg = lst_colour_beg[k]
		}
	}
document.getElementById("sectors").style.display = val_beg[0];
document.getElementById("uses").style.display = val_beg[1];
document.getElementById("criteria").style.display = val_beg[2];
document.getElementById("stl").style.display = val_beg[3];
ong_sec.style.backgroundColor = colour_beg[0];
ong_use.style.backgroundColor = colour_beg[1];
ong_cri.style.backgroundColor = colour_beg[2];
ong_stl.style.backgroundColor = colour_beg[3];
}

/*Sheet change of master*/

var ina = 'rgba(120,120,120,1)';
var ac = 'rgba(170,30,120,1)';
var done = 'rgba(135,25,96,1)';

function switch_mas(onglet)
{
if (onglet=='cri')
	{
	document.getElementById("criteria").style.display = 'grid';
	document.getElementById("stl").style.display = 'none';
	ong_cri.style.backgroundColor = ac;
	ong_stl.style.backgroundColor = ina;
	}
if (onglet=='stl') 
	{
	document.getElementById("criteria").style.display = 'none';
	document.getElementById("stl").style.display = 'grid';
	ong_cri.style.backgroundColor = done;
	ong_stl.style.backgroundColor = ac;
	}
}

/*Sheet change of results*/

var ina = 'rgba(120,120,120,1)';
var ac = 'rgba(170,30,120,1)';
var done = 'rgba(135,25,96,1)';

function switch_res(onglet)
{
if (onglet=='res') 
	{
	document.getElementById("strategy_user").style.display = 'grid';
	document.getElementById("rules").style.display = 'none';
	document.getElementById("set_machine").style.display = 'none';
	ong_res.style.backgroundColor = ac;
	ong_rul.style.backgroundColor = ina;
	ong_set.style.backgroundColor = ina;
	}
else if (onglet=='rul')
	{
	document.getElementById("strategy_user").style.display = 'none';
	document.getElementById("rules").style.display = 'grid';
	document.getElementById("set_machine").style.display = 'none';
	ong_res.style.backgroundColor = done;
	ong_rul.style.backgroundColor = ac;
	ong_set.style.backgroundColor = ina ;
	}
else if (onglet=='set') 
	{
	document.getElementById("strategy_user").style.display = 'none';
	document.getElementById("rules").style.display = 'none';
	document.getElementById("set_machine").style.display = 'grid';
	ong_res.style.backgroundColor = done;
	ong_rul.style.backgroundColor = done;
	ong_set.style.backgroundColor = ac;
	}
}

/*Strategy of printing*/

function strategy(str)
{
var result_mate = document.getElementsByClassName("material_choice");
var result_cost = document.getElementsByClassName("cost_choice");
for (var n=0; n<result_mate.length; n++) 
	{
	result_mate[n].style.display = 'none';
	result_cost[n].style.display = 'none';
	}
if (str=='mate')
	{
	for (var n=0; n<result_mate.length; n++) 
		{
		result_mate[n].style.display = 'inline-block';
		result_cost[n].style.display = 'none';
		}	
	}
if (str=='cost')
	{
	for (var n=0; n<result_cost.length; n++) 
		{
		result_mate[n].style.display = 'none';
		result_cost[n].style.display = 'inline-block';
		}
	}
}

/*strategy change colors*/

var in_stra=[0,0];
var lst_stra=['mate','cost'];
var sha_ina = "0 9px grey";
var sha_ac = "0 9px green";

function change_colour_strategy(stra)
{
for (var k=0; k<lst_stra.length; k++)
	{
	if (lst_stra[k]==stra)
		{
		lst_img_stra= ['inline-block', 'none', 'inline-block', 'none'];
		checked=[false,false];
		shadow=[sha_ina,sha_ina];
		if (in_stra[k]==0)
			{
			in_stra=[0,0];
			in_stra[k]=1;
			shadow[k]=sha_ac;
			checked[k]=true;
			lst_img_stra[2*k]='none';
			lst_img_stra[(2*k)+1]='inline-block';
			}
		else
			{
			in_stra=[0,0];
			}
		}
	}
document.getElementById("img_mate_ina").style.boxShadow = shadow[0];
document.getElementById("img_cost_ina").style.boxShadow = shadow[1];
document.getElementById("img_mate_ac").style.boxShadow = shadow[0];
document.getElementById("img_cost_ac").style.boxShadow = shadow[1];
document.getElementById("img_mate_ina").style.display = lst_img_stra[0];
document.getElementById("img_cost_ina").style.display = lst_img_stra[2];
document.getElementById("img_mate_ac").style.display = lst_img_stra[1];
document.getElementById("img_cost_ac").style.display = lst_img_stra[3];
}

var use = 'othe';

function opti_criteria(cate, valeur)
{
	if ((cate=='sect') && ((valeur=='medi')||(valeur=="aero")||(valeur=="auto")||(valeur=="luxe")||(valeur=="oil")))
	{
		use=valeur;
	}
	else if ((cate=='sect') && (valeur=='othe'))
	{
		use='othe';
		change_colour_colo('empty');
		change_material('empty');
		change_surface('empty');
		change_colour_filling('empty');
		change_colour_ther('empty');
		change_colour_opti('empty');
		change_colour_spee('empty');
		change_technology('empty');
	}
	else if ((cate=='uses') && (valeur=='chan'))
	{
		change_colour_colo('empty');
		change_material('empty');
		change_surface('empty');
		change_colour_filling('empty');
		change_colour_ther('empty');
		change_colour_opti('empty');
		change_colour_spee('empty');
		change_technology('empty');
	}
	else if (cate=='uses')
	{
		if ((use=='medi') && (valeur=='ergo'))
		{
			change_technology('tec1');
			change_technology('tec2');
			change_technology('tec3');
			change_technology('tec4');
			change_technology('tec4');
			change_technology('tec5');
			change_technology('tec6');
			change_technology('tec6');
			change_technology('tec7');
			change_technology('tec7');
			change_material('mate_1');
			change_material('mate_2');
			change_material('mate_2');
			change_material('mate_3');
			change_material('mate_4');
			change_surface('fair');
			change_colour_filling('emp');
			change_colour_colo('mono');
			change_colour_ther('no');
			change_colour_opti('no');
			change_colour_spee('yes');
		}
		else if ((use=='medi') && (valeur=='func'))
		{			
			change_technology('tec1');change_technology('tec1');
			change_technology('tec2');change_technology('tec2');
			change_technology('tec3');
			change_technology('tec4');
			change_technology('tec5');
			change_technology('tec6');
			change_technology('tec7');change_technology('tec7');
			change_material('mate_1');
			change_material('mate_2');
			change_material('mate_3');change_material('mate_3');
			change_material('mate_4');change_material('mate_4');
			change_surface('fair');
			change_colour_filling('ful');
			change_colour_colo('mono');
			change_colour_ther('no');
			change_colour_opti('yes');
			change_colour_spee('yes');
		}
		else if ((use=='aero') && (valeur=='asse'))
		{
			change_technology('tec1');change_technology('tec1');
			change_technology('tec2');change_technology('tec2');
			change_technology('tec3');
			change_technology('tec4');
			change_technology('tec5');
			change_technology('tec6');
			change_technology('tec7');change_technology('tec7');
			change_material('mate_1');
			change_material('mate_2');
			change_material('mate_3');change_material('mate_3');
			change_material('mate_4');change_material('mate_4');
			change_surface('fair');
			change_colour_filling('emp');
			change_colour_colo('mono');
			change_colour_ther('no');
			change_colour_opti('no');
			change_colour_spee('yes');
		}
		else if ((use=='aero') && (valeur=='func'))
		{
			change_technology('tec1');change_technology('tec1');
			change_technology('tec2');change_technology('tec2');
			change_technology('tec3');
			change_technology('tec4');
			change_technology('tec5');
			change_technology('tec6');
			change_technology('tec7');change_technology('tec7');
			change_material('mate_1');
			change_material('mate_2');
			change_material('mate_3');change_material('mate_3');
			change_material('mate_4');change_material('mate_4');
			change_surface('fair');
			change_colour_filling('ful');
			change_colour_colo('mono');
			change_colour_ther('yes');
			change_colour_opti('yes');
			change_colour_spee('yes');
		}
		else if ((use=='auto') && (valeur=='asse'))
		{
			change_technology('tec1');change_technology('tec1');
			change_technology('tec2');change_technology('tec2');
			change_technology('tec3');
			change_technology('tec4');
			change_technology('tec5');
			change_technology('tec6');
			change_technology('tec7');change_technology('tec7');
			change_material('mate_1');
			change_material('mate_2');
			change_material('mate_3');
			change_material('mate_3');
			change_material('mate_4');
			change_surface('fair');
			change_colour_filling('emp');
			change_colour_colo('mono');
			change_colour_ther('no');
			change_colour_opti('no');
			change_colour_spee('yes');
		}
		else if ((use=='auto') && (valeur=='func'))
		{
			change_technology('tec1');change_technology('tec1');
			change_technology('tec2');change_technology('tec2');
			change_technology('tec3');
			change_technology('tec4');
			change_technology('tec5');
			change_technology('tec6');
			change_technology('tec7');change_technology('tec7');
			change_material('mate_1');
			change_material('mate_2');
			change_material('mate_3');change_material('mate_3');
			change_material('mate_4');
			change_surface('fair');
			change_colour_filling('ful');
			change_colour_colo('mono');
			change_colour_ther('yes');
			change_colour_opti('yes');
			change_colour_spee('yes');
		}
		else if ((use=='luxu') && (valeur=='ergo'))
		{
			change_technology('tec1');
			change_technology('tec2');
			change_technology('tec3');change_technology('tec4');
			change_technology('tec4');
			change_technology('tec5');
			change_technology('tec6');change_technology('tec6');
			change_technology('tec7');change_technology('tec7');
			change_material('mate_1');
			change_material('mate_2');change_material('mate_2');
			change_material('mate_3');
			change_material('mate_4');
			change_surface('fair');
			change_colour_filling('emp');
			change_colour_colo('mono');
			change_colour_ther('no');
			change_colour_opti('no');
			change_colour_spee('yes');
		}
		else if ((use=='luxu') && (valeur=='esth'))
		{
			change_technology('tec1');
			change_technology('tec2');
			change_technology('tec3');
			change_technology('tec4');change_technology('tec4');
			change_technology('tec5');
			change_technology('tec6');change_technology('tec6');
			change_technology('tec7');change_technology('tec7');
			change_material('mate_1');
			change_material('mate_2');change_material('mate_2');
			change_material('mate_3');
			change_material('mate_4');
			change_surface('good');
			change_colour_filling('emp');
			change_colour_colo('mult');
			change_colour_ther('no');
			change_colour_opti('no');
			change_colour_spee('yes');
		}
		else if ((use=='oil') && (valeur=='asse'))
		{
			change_technology('tec1');change_technology('tec1');
			change_technology('tec2');change_technology('tec2');
			change_technology('tec3');
			change_technology('tec4');
			change_technology('tec5');
			change_technology('tec6');
			change_technology('tec7');change_technology('tec7');
			change_material('mate_1');
			change_material('mate_2');
			change_material('mate_3');change_material('mate_3');
			change_material('mate_4');change_material('mate_4');
			change_surface('fair');
			change_colour_filling('emp');
			change_colour_colo('mono');
			change_colour_ther('no');
			change_colour_opti('no');
			change_colour_spee('yes');
		}
		else if ((use=='oil') && (valeur=='func'))
		{
			change_technology('tec1');change_technology('tec1');
			change_technology('tec2');change_technology('tec2');
			change_technology('tec3');
			change_technology('tec4');
			change_technology('tec5');
			change_technology('tec6');
			change_technology('tec7');change_technology('tec7');
			change_material('mate_1');
			change_material('mate_2');
			change_material('mate_3');change_material('mate_3');
			change_material('mate_4');change_material('mate_4');
			change_surface('fair');
			change_colour_filling('ful');
			change_colour_colo('mono');
			change_colour_ther('yes');
			change_colour_opti('yes');
			change_colour_spee('yes');
		}
	}
}