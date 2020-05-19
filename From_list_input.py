import crypt
import copy

def main():

    org_dict = {'sam':'egg', 'kate':'cat', "mom": 'food', "dad": "golf", 'connor': 'tennis'}
    word_list = ['egg', 'random', 'cat','tennis','this','argument', 'food', 'golf']

    print(solve_passwd(create_enc(org_dict), create_test_words(word_list)))

def create_enc(pass_dict):    ## creating a dicitionary of encrypted passwd
    new_value_list = []
    pass_list = list(pass_dict.values())
    key_list = list(pass_dict.keys())
    for i in pass_list:
        new_value = crypt.crypt(i, 'HX')
        new_value_list.append(new_value)

    final_org_dict = {key_list[i] : new_value_list[i] for i in range(len(key_list))}
    return final_org_dict
def create_test_words(test_word_list): ##encrypting the list so we can match it to the originaal list
    value_list = []
    for i in test_word_list:
        new_value = crypt.crypt(i, 'HX')
        value_list.append(new_value)
    test_words_dict = {value_list[i]: test_word_list[i] for i in range(len(value_list))}
    return test_words_dict

def solve_passwd(final_org_dict, test_word_dict):
    value_list = [] ## this is where i will put the cracked the values compared to the test word values
    final_org_list = list(final_org_dict.values()) ##this is a list of encrypted passwords
    test_word_list = list(test_word_dict.keys()) ##this is a list of encrypted passwords in regards to passwords listed in words list, i will use this to plug it into test_word_dict to crack the passwords
    ult_key_list = list(final_org_dict.keys())  ## this is when all passwd returns
    new_org_dict = {v: k for k, v in final_org_dict.items()} ## this is reversing the dict for the values that are not in test_word_list
    for x in final_org_list:
        if x in test_word_list:

            value = test_word_dict[x]
            value_list.append(value)


        else:

            del new_org_dict[x]


    ult_key_list = list(new_org_dict.values())

    final_passwd_dict = {ult_key_list[i]: value_list[i] for i in range(len(ult_key_list))}
    return final_passwd_dict







if __name__ == '__main__':
    main()





