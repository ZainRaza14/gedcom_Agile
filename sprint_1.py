from userStory04 import user_story04
from userStory08 import user_story08
from userStory03 import us03_birth_b4_death
from userStory06 import us06_divo_b4_death
from userStory01 import us01_dates_b4_curr_date
from userStory05 import us05_marr_b4_death

from print_main import printTables

def sprint_1_user_stories():
    master_file_name="finalfamtree.ged"
    indTable,famTable= printTables(master_file_name)
    error_list = []
    error_list.extend(us01_dates_b4_curr_date(master_file_name))
    '''
    error_list.extend(user_story02(master_file_name)) 
    error_list.extend(user_story03(master_file_name)) 
    '''
    
    error_list.extend(us03_birth_b4_death(master_file_name))
    error_list.extend(user_story04(master_file_name))
    error_list.extend(us05_marr_b4_death(master_file_name))
    '''
    error_list.extend(user_story06(master_file_name)) 
    error_list.extend(user_story07(master_file_name)) 
    '''
    
    error_list.extend(us06_divo_b4_death(master_file_name))
    error_list.extend(user_story08(master_file_name)) 
    
    
    
    for each_error in error_list:
        print(each_error)
    
    with open('sprint1output.txt','w') as file:
        file.write('\n\nIndividuals Information----------------------->\n')
        file.write(indTable.get_string())
        file.write("\n")
        file.write('\n\nFamily Information----------------------->\n')
        file.write(famTable.get_string())
        file.write("\n")
        for each_error in error_list:
            file.write(each_error+"\n")
        
        
        

    

if __name__ == "__main__":
    sprint_1_user_stories()