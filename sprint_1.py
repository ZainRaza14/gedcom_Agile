from userStory04 import us04_marr_b4_divo
from userStory08 import us08_birth_b4_marr_parents
from userStory03 import us03_birth_b4_death
from userStory06 import us06_divo_b4_death
from userStory01 import us01_dates_b4_curr_date
from userStory05 import us05_marr_b4_death
from print_main import printTables

def sprint_1_user_stories():
    master_file_name="finalfamtree.ged"
    printTables(master_file_name)
    error_list = []
    error_list.extend(us01_dates_b4_curr_date(master_file_name))
    '''
    error_list.extend(user_story02(master_file_name)) 
    error_list.extend(user_story03(master_file_name)) 
    '''
    
    error_list.extend(us03_birth_b4_death(master_file_name))
    error_list.extend(us04_marr_b4_divo(master_file_name)) 
    error_list.extend(us05_marr_b4_death(master_file_name)) 
    '''
    error_list.extend(user_story06(master_file_name)) 
    error_list.extend(user_story07(master_file_name)) 
    '''
    
    error_list.extend(us06_divo_b4_death(master_file_name))
    error_list.extend(us08_birth_b4_marr_parents(master_file_name)) 
    
    for each_error in error_list:
        print(each_error)

    

if __name__ == "__main__":
    sprint_1_user_stories()