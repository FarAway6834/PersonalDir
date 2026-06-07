import aka
from sympy.abc import a, b
from attrname import getnames, show_dict, show_list, show_dict_and_list_reqly, dictzip

def sympyic_getnames(x):
    x_names = getnames(x)
    x_names["nonv"] = {"isxxx" : [name for name in x_names["nonv"] if name[:3] == "is_"], "xxx" : [name for name in x_names["nonv"] if name[:3] != "is_"]}
    
    x_names["test"] = {"{getattr(self, name) in [True, False, None] for name in sympyic_getnames(self)['nonv']['isxxx']}" : {getattr(a, name) in [True, False, None] for name in x_names['nonv']['isxxx']}, "sympyic_getnames(self)['v']['f'] == []" : (x_names['v']['f'] == [])}
    
    x_names["v"]["m"] = {"isxxx" : [name for name in x_names["v"]["m"] if name[:3] == "is_"], "asxxx" : [name for name in x_names["v"]["m"] if name[:3] == "as_"], "extracts" : [name for name in x_names["v"]["m"] if name[:8] == "extract_"], "xxx" : [name for name in x_names["v"]["m"] if name[:3] not in ["is_", "as_"] and name[:8] != "extract_"]}
    
    x_names["test"]["show_dict_and_list_reqly(sympyic_getnames(self)['v']['m'], multiline = True)"] = show_dict_and_list_reqly(x_names['v']['m'], multiline = True)

    return x_names

a_names = sympyic_getnames(a)

c = a_plus_b = a + b
c_names = sympyic_getnames(c)
