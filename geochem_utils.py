import pandas as pd
import re




def clean_oxides(df, element_col_name, result_col_name):
    """
    This function converts all oxides listed in oxides_list to their base element.
    It converts both the actual name, and all its corresponding assay result
    
    Example:
    If we have a assay result as Al2O3 - 200ppm,
    It becomes Al - 200 /1.8895 ppm
    
    Inputs:
    df (pandas dataframe) - geochem dataframe
    element_col_name (string) - name of the column that contains the element names
    result_col_name (string) - name of the column that conatins the assay results
    
    Returns:
    df
    
    
    
    """
    
    
    
    
    oxides_list = {'Al2O3' : 1.8895,
        'As2O3':     1.3203,
        'BaO' : 1.1165,
        'Bi2O3'   :      1.1148,              
        'CaO' : 1.3392,
        'CaCO3' :      2.5, 
        'CeO2':    1.2284,
        'Cr2O3' : 1.1415,
        'CoO'   :      1.2715,           
        'CuO'   :      1.2518,
        'Cs2O'   :     1.0602,           
        'FeO'    :   1.2865,
        'Fe2O3' : 1.4297,
        'HfO2' :          1.1793,           
        'K2O' : 1.2046,
        'La2O3':    1.1728,
        'Li2O':    2.1527,
        'MgO' : 1.6582,
        'MnO' : 1.2912,
        'Na2O' : 1.3480,
        'Nb2O5':    1.4305,           
        'NiO'  :          1.2725,
        'PbO':    1.0772,
        'P2O5' : 2.2916,
        'Rb2O'   :     1.0936,
        'Sb2O3':    1.197103,           
        'SiO2' : 2.1392,
        'SnO2' : 1.2696,
        'SrO' : 1.1826,
        'Ta2O5':    1.2211,           
        'ThO2':     1.1379,
        'TiO2' : 1.6681,
        'eU3O8' : 1.1792,
        'U3O8' : 1.1792,
        'WO3'   :       1.2610,
        'V2O5' : 1.7852,
        'Y2O3'  :    1.2699 ,
        'ZnO'  :         1.2448,           
        'ZrO2' : 1.3508
        }

    for oxide, conv in oxides_list.items():
        #Get base element
        #Split on Oxygen simple, grab first part and then replace any numbers with nothing

        if oxide == 'CaCO3':
            base_ele = 'Ca'
        elif oxide == 'eU3O8':
            base_ele = 'U'
        else:
            base_ele = re.sub( '\d', '' , oxide.split('O')[0])
        #print("Converting {} to {}".format(oxide, base_ele))
        mask = df[element_col_name] == oxide
        df.loc[mask, element_col_name] = base_ele
        df.loc[mask, result_col_name] = df.loc[mask, result_col_name].copy() / conv
        
    return df
