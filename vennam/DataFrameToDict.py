def dftodict(dataframe):
    """This function takes the dataframe
    as a parameter and convert to dictionary """

    dummy_dict={key:"" for key in dataframe.columns.to_list()}
    dummy_dict_lst=[]
    for index,row in dataframe.iterrows():
        dummy_dict1={key:row[key] for key in dummy_dict.keys()}
        dummy_dict_lst.append(dummy_dict1.copy())
    return dummy_dict_lst
  