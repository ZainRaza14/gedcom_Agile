#sprint2
from userstories.sprint02_us.userStory12 import us12_parents_not_too_old
from userstories.sprint02_us.userStory13 import us13_siblings_spacing
from userstories.sprint02_us.userStory09 import us09_birth_b4_parents_death
from userstories.sprint02_us.userStory16 import us16_male_last_names
from userstories.sprint02_us.userStory11 import us11_no_bigamy
from userstories.sprint02_us.userStory14 import us14_multiple_births
from userstories.sprint02_us.userStory10 import us10_marr_after_14
from userstories.sprint02_us.userStory15 import us15_fewer_than_15_siblings


#sprin1
from userstories.sprint01_us.userStory04 import us04_marr_b4_divo
from userstories.sprint01_us.userStory08 import us08_birth_b4_marr_parents
from userstories.sprint01_us.userStory03 import us03_birth_b4_death
from userstories.sprint01_us.userStory06 import us06_divo_b4_death
from userstories.sprint01_us.userStory02 import us02_birth_b4_marr
from userstories.sprint01_us.userStory07 import us07_less_than_150years
from userstories.sprint01_us.userStory01 import us01_dates_b4_curr_date
from userstories.sprint01_us.userStory05 import us05_marr_b4_death

from print_main import printTables

def sprint_2_user_stories():
    master_file_name="gedfilestest/sprint02-testdata_2_CHECK.ged"
    indTable,famTable= printTables(master_file_name)
    error_list = []
    
    #sprint1
    error_list.extend(us01_dates_b4_curr_date(master_file_name)) 
    error_list.extend(us02_birth_b4_marr(master_file_name)) 
    error_list.extend(us03_birth_b4_death(master_file_name))
    error_list.extend(us04_marr_b4_divo(master_file_name)) 
    error_list.extend(us05_marr_b4_death(master_file_name))  
    error_list.extend(us06_divo_b4_death(master_file_name))
    error_list.extend(us07_less_than_150years(master_file_name))
    error_list.extend(us08_birth_b4_marr_parents(master_file_name))
    
    #sprint2
    error_list.extend(us09_birth_b4_parents_death(master_file_name))
    error_list.extend(us10_marr_after_14(master_file_name))
    error_list.extend(us11_no_bigamy(master_file_name))
    error_list.extend(us12_parents_not_too_old(master_file_name))
    error_list.extend(us13_siblings_spacing(master_file_name))
    error_list.extend(us14_multiple_births(master_file_name))
    error_list.extend(us15_fewer_than_15_siblings(master_file_name))
    error_list.extend(us16_male_last_names(master_file_name))

    for each_error in error_list:
        print(each_error)
    
    with open('sprint2output.txt','w') as file:
        file.write('\n\nIndividuals Information----------------------->\n')
        file.write(indTable.get_string())
        file.write("\n")
        file.write('\n\nFamily Information----------------------->\n')
        file.write(famTable.get_string())
        file.write("\n")
        for each_error in error_list:
            file.write(each_error+"\n")
        
        
if __name__ == "__main__":
    sprint_2_user_stories()