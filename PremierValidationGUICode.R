library(reticulate)
library(taskscheduleR)
library(shiny)
library(miniUI)


#py_run_file("PythonPremierValidation.py")
#py_run_string("browser.quit()")
#py_run_file("PremierBatchReports.py")
#py_run_file("PremierValidTest.py")
sites <- c("MSH","MSBI","MSSL","MSW")
SelectedSites <- select.list(sites, graphics = T, multiple = T)
if (length(SelectedSites) != 0){
  write("Selected Sites:", file="PremierVariables.txt", append=T)
  write(SelectedSites, file="PremierVariables.txt",append=TRUE)
} else{
  print("No site was selected")
}

Hour <- c("12:", "01:", "02:", "03:", "04:")
Minute <- c("00" ,"05", "10","15" , "20")
SelectedHour <-select.list(Hour, graphics = T, multiple = F)
SelectedMinute <- select.list(Minute, graphics = T, multiple = F)
CombinedTime <- paste0(SelectedHour,SelectedMinute)
if (CombinedTime != ""){
  write("Automation Time:", file ="PremierVariables.txt", append=T)
  write(CombinedTime, file ="PremierVariables.txt", append=T)
  } else{
  print("No time was selected")
}


#R <- selectInput("Test", "Test: " ,
#            c("MSBI" = "MSBI",
#              "MSH" = "MSH"))
#print(Test)



#myscript <-"C:/Users/Administrator/Documents/helloworld.R"
#Rpath <- "C:/Program Files/R/R-3.6.2/bin/Rscript.exe"

#taskscheduler_create(taskname = "TestTaskScheduleR", rscript = myscript, schedule="ONCE", starttime= format(Sys.time() + 62, "%H:%M" ))
