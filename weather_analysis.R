
library(stringr)
Dir = 'weather_claudio.csv'
df  <- read.csv(Dir, sep = ",", stringsAsFactors = FALSE) #stringAsFactors

df <- df[,2:7]


df$day <- as.Date(df$day,format='%b %d')


df$precip<- str_extract(df$precip, "\\-*\\d+\\.*\\d*") #prec em %
df$wind <- str_extract(df$wind, "\\-*\\d+\\.*\\d*") #wind em km/h
df$humidity <- str_extract(df$humidity, "\\-*\\d+\\.*\\d*") #em %
df[1,3] <- "32º19º"



df$maxTemp <- str_extract(df$temp, "\\-*\\d+\\.*\\d*") 


df_temp <- data.frame(matrix(unlist(regmatches(df$temp,gregexpr("[[:digit:]]+\\.*[[:digit:]]*",df$temp))), nrow=15, byrow=T))
colnames(df_temp) <- c('maxTemp','minTemp')
df$temp <- NULL 

final_df <- cbind(df, df_temp)

