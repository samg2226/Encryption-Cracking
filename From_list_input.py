import crypt
import copy

def main():

    Original_Dictionary = {'sam':'egg', 'kate':'cat', "mom": 'food', "dad": "golf", 'connor': 'tennis'}
    English_Words_To_Test = ['egg', 'random', 'cat','tennis','this','argument', 'food', 'golf']

    print(solve_passwd(create_enc(Original_Dictionary), create_test_words(English_Words_To_Test)))

def create_enc(Dict_To_Enc):    ## creating a dicitionary of encrypted passwd
    English_Word_List = []
    English_Values_Of_Dict = list(Dict_To_Enc.values())
    Key_List_To_Dict_To_Enc = list(Dict_To_Enc.keys())
    for i in English_Values_Of_Dict:
        new_value = crypt.crypt(i, 'HX')
        English_Word_List.append(new_value)

    Enc_Original_Dict = {Key_List_To_Dict_To_Enc[i] : English_Word_List[i] for i in range(len(Key_List_To_Dict_To_Enc))}
    return Enc_Original_Dict
def create_test_words(test_word_list): ##encrypting the list so we can match it to the originaal list
    Keys_Enc_Value_List = []
    for i in test_word_list:
        new_value = crypt.crypt(i, 'HX')
        Keys_Enc_Value_List.append(new_value)
    Test_Words_Dict = {Keys_Enc_Value_List[i]: test_word_list[i] for i in range(len(Keys_Enc_Value_List))}
    return Test_Words_Dict

def solve_passwd(enc_org_dict, test_word_dict):
    Values_To_Final_Dict = [] ## this is where i will put the cracked the values compared to the test word values
    enc_org_dict_values = list(enc_org_dict.values()) ##this is a list of encrypted passwords
    test_word_list = list(test_word_dict.keys()) ##this is a list of encrypted passwords in regards to passwords listed in words list, i will use this to plug it into test_word_dict to crack the passwords
    ult_key_list = list(enc_org_dict.keys())  ## this is when all passwd returns
    new_org_dict = {v: k for k, v in enc_org_dict.items()} ## this is reversing the dict for the values that are not in test_word_list
    for x in enc_org_dict_values:
        if x in test_word_list:

            value = test_word_dict[x]
            Values_To_Final_Dict.append(value)


        else:

            del new_org_dict[x]


    ult_key_list = list(new_org_dict.values())

    final_passwd_dict = {ult_key_list[i]: Values_To_Final_Dict[i] for i in range(len(ult_key_list))}
    return final_passwd_dict







if __name__ == '__main__':
    main()





