def clean_data(data):
    """
    TODO: Implement your "clean_heartrate_data" function from TLAB #1 & #2
    within this module. Note that this code will be *slightly* different
    from your original function.
    
    We need to skip that 8th (aka first) row.
    """
    clean_data_lst = []
    for row in data:
        if row !="minutes\n":
            clean_data_lst.append(float(row.strip()))
    
    return clean_data_lst