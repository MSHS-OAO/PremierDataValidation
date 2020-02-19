library(reticulate)
library(taskscheduleR)
library(shiny)
library(miniUI)


#py_run_file("PythonPremierValidation.py")
#py_run_string("browser.quit()")
#py_run_file("PremierBatchReports.py")
#py_run_file("PremierValidTest.py")
sites <- c("MSH","MSBI","MSSL","MSW")
SelectedSites <- select.list(sites, graphics = T, multiple = T, title = "Select Site")
if (length(SelectedSites) != 0){
  write("Selected Sites:", file="PremierVariables.txt", append=T)
  write(SelectedSites, file="PremierVariables.txt",append=TRUE)
} else{
  print("No site was selected")
}

Hour <- c("0:", "1:", "2:", "3:", "4:")
Minute <- c("00" ,"05", "10","15" , "20")
SelectedHour <-select.list(Hour, graphics = T, multiple = F, title = "Select Hour")
SelectedMinute <- select.list(Minute, graphics = T, multiple = F, title = "Select Minute")
CombinedTime <- paste0(SelectedHour,SelectedMinute)
if (CombinedTime != ""){
  write("Automation Time:", file ="PremierVariables.txt", append=T)
  write(CombinedTime, file ="PremierVariables.txt", append=T)
  } else{
  print("No time was selected")
}


