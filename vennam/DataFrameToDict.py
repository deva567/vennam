def dftodict(dataframe):
    """This function takes the dataframe
    as a parameter and convert to dictionary """

    tmp_dict={key:"" for key in dataframe.columns.to_list()}
    tmp_dict_lst=[]
    for index,row in dataframe.iterrows():
        tmp_dict1={key:row[key] for key in tmp_dict.keys()}
        tmp_dict_lst.append(tmp_dict1.copy())
    return tmp_dict_lst
  
