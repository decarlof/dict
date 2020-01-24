import numpy as np

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    value = "{0:4.2f}".format(array[idx])
    return value


def main():

    lookup={
    "55.00" : {"Mirr_Ang": 1.200, "Mirr_YAvg":  0.2, "DMM_USY_OB": -5.1, "DMM_USY_IB": -5.1, "DMM_DSY": -5.1, "USArm": 0.95, "DSArm": 0.973 , "M2Y": 11.63, "DMM_USX":27.5, "DMM_DSX": 27.5, "XIASlitY": 21.45},           
    "50.00" : {"Mirr_Ang": 1.500, "Mirr_YAvg": -0.2, "DMM_USY_OB": -5.1, "DMM_USY_IB": -5.1, "DMM_DSY": -5.1, "USArm": 1.00, "DSArm": 1.022 , "M2Y": 12.58, "DMM_USX":27.5, "DMM_DSX": 27.5, "XIASlitY": 24.05},           
    "45.00" : {"Mirr_Ang": 1.500, "Mirr_YAvg": -0.2, "DMM_USY_OB": -5.1, "DMM_USY_IB": -5.1, "DMM_DSY": -5.1, "USArm": 1.05, "DSArm": 1.072 , "M2Y": 13.38, "DMM_USX":27.5, "DMM_DSX": 27.5, "XIASlitY": 25.05},           
    "40.00" : {"Mirr_Ang": 1.500, "Mirr_YAvg": -0.2, "DMM_USY_OB": -5.1, "DMM_USY_IB": -5.1, "DMM_DSY": -5.1, "USArm": 1.10, "DSArm": 1.124 , "M2Y": 13.93, "DMM_USX":27.5, "DMM_DSX": 27.5, "XIASlitY": 23.35},           
    "35.00" : {"Mirr_Ang": 2.000, "Mirr_YAvg": -0.2, "DMM_USY_OB": -3.8, "DMM_USY_IB": -3.8, "DMM_DSY": -3.7, "USArm": 1.25, "DSArm": 1.2745, "M2Y": 15.57, "DMM_USX":27.5, "DMM_DSX": 27.5, "XIASlitY": 26.35},           
    "31.00" : {"Mirr_Ang": 2.657, "Mirr_YAvg":  0.0, "DMM_USY_OB": -0.1, "DMM_USY_IB": -0.1, "DMM_DSY": -0.1, "USArm": 1.10, "DSArm": 1.121 , "M2Y": 12.07, "DMM_USX":82.5, "DMM_DSX": 82.5, "XIASlitY": 28.35},           
    "27.40" : {"Mirr_Ang": 2.657, "Mirr_YAvg":  0.0, "DMM_USY_OB": -0.1, "DMM_USY_IB": -0.1, "DMM_DSY": -0.1, "USArm": 1.15, "DSArm": 1.169 , "M2Y": 13.71, "DMM_USX":82.5, "DMM_DSX": 82.5, "XIASlitY": 29.35},           
    "24.90" : {"Mirr_Ang": 2.657, "Mirr_YAvg": -0.2, "DMM_USY_OB": -0.1, "DMM_USY_IB": -0.1, "DMM_DSY": -0.2, "USArm": 1.20, "DSArm": 1.2235, "M2Y": 14.37, "DMM_USX":82.5, "DMM_DSX": 82.5, "XIASlitY": 30.35},           
    "22.70" : {"Mirr_Ang": 2.657, "Mirr_YAvg":  0.0, "DMM_USY_OB": -0.1, "DMM_USY_IB": -0.1, "DMM_DSY": -0.1, "USArm": 1.25, "DSArm": 1.271 , "M2Y": 15.57, "DMM_USX":82.5, "DMM_DSX": 82.5, "XIASlitY": 31.35},           
    "21.10" : {"Mirr_Ang": 2.657, "Mirr_YAvg":  0.0, "DMM_USY_OB": -0.1, "DMM_USY_IB": -0.1, "DMM_DSY": -0.1, "USArm": 1.30, "DSArm": 1.3225, "M2Y": 15.67, "DMM_USX":82.5, "DMM_DSX": 82.5, "XIASlitY": 32.35},           
    "20.20" : {"Mirr_Ang": 2.657, "Mirr_YAvg":  0.0, "DMM_USY_OB": -0.1, "DMM_USY_IB": -0.1, "DMM_DSY": -0.1, "USArm": 1.35, "DSArm": 1.373 , "M2Y": 17.04, "DMM_USX":82.5, "DMM_DSX": 82.5, "XIASlitY": 33.35},           
    "18.90" : {"Mirr_Ang": 2.657, "Mirr_YAvg":  0.0, "DMM_USY_OB": -0.1, "DMM_USY_IB": -0.1, "DMM_DSY": -0.1, "USArm": 1.40, "DSArm": 1.4165, "M2Y": 17.67, "DMM_USX":82.5, "DMM_DSX": 82.5, "XIASlitY": 34.35},           
    "17.60" : {"Mirr_Ang": 2.657, "Mirr_YAvg":  0.0, "DMM_USY_OB": -0.1, "DMM_USY_IB": -0.1, "DMM_DSY": -0.1, "USArm": 1.45, "DSArm": 1.472 , "M2Y": 18.89, "DMM_USX":82.5, "DMM_DSX": 82.5, "XIASlitY": 34.35},           
    "16.80" : {"Mirr_Ang": 2.657, "Mirr_YAvg":  0.0, "DMM_USY_OB": -0.1, "DMM_USY_IB": -0.1, "DMM_DSY": -0.1, "USArm": 1.50, "DSArm": 1.5165, "M2Y": 19.47, "DMM_USX":82.5, "DMM_DSX": 82.5, "XIASlitY": 52.35},           
    "16.00" : {"Mirr_Ang": 2.657, "Mirr_YAvg":  0.0, "DMM_USY_OB": -0.1, "DMM_USY_IB": -0.1, "DMM_DSY": -0.1, "USArm": 1.55, "DSArm": 1.568 , "M2Y": 20.57, "DMM_USX":82.5, "DMM_DSX": 82.5, "XIASlitY": 53.35},           
    "15.00" : {"Mirr_Ang": 2.657, "Mirr_YAvg":  0.0, "DMM_USY_OB": -0.1, "DMM_USY_IB": -0.1, "DMM_DSY": -0.1, "USArm": 1.60, "DSArm": 1.6195, "M2Y": 21.27, "DMM_USX":82.5, "DMM_DSX": 82.5, "XIASlitY": 54.35},           
    "14.40" : {"Mirr_Ang": 2.657, "Mirr_YAvg":  0.0, "DMM_USY_OB": -0.1, "DMM_USY_IB": -0.1, "DMM_DSY": -0.1, "USArm": 1.65, "DSArm": 1.67  , "M2Y": 22.27, "DMM_USX":82.5, "DMM_DSX": 82.5, "XIASlitY": 51.35}            
    }

    energy = 37
    energies_str = np.array(list(lookup.keys())[:])
    energies_flt = [float(i) for i in  energies_str]

    energy_calibrated = find_nearest(energies_flt, energy)
    print(energy, energy_calibrated)
    print(lookup[energy_calibrated]["Mirr_Ang"])


    Mirr_Ang = lookup[energy_calibrated]["Mirr_Ang"]
    Mirr_YAvg = lookup[energy_calibrated]["Mirr_YAvg"]

    DMM_USY_OB = lookup[energy_calibrated]["DMM_USY_OB"] 
    DMM_USY_IB = lookup[energy_calibrated]["DMM_USY_IB"]
    DMM_DSY = lookup[energy_calibrated]["DMM_DSY"]

    USArm = lookup[energy_calibrated]["USArm"]                
    DSArm = lookup[energy_calibrated]["DSArm"]

    M2Y = lookup[energy_calibrated]["M2Y"]
    DMM_USX = lookup[energy_calibrated]["DMM_USX"]
    DMM_DSX = lookup[energy_calibrated]["DMM_DSX"]
    XIASlitY = lookup[energy_calibrated]["XIASlitY"]   


    
if __name__ == '__main__':
    main()


 



















    
    


































 
    

















    

















    
















    




