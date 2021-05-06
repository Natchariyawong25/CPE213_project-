# -*- coding: utf-8 -*-
"""cpe213_term_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y7Jgwj4JUKy7up78sV7WxamXW-75Tnso

# **Introduction to problem**
<img src="https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/articles/health_tools/did_you_know_this_could_lead_to_heart_disease_slideshow/493ss_thinkstock_rf_heart_illustration.jpg">
<br>
โรคหัวใจและหลอดเลือด เป็นกลุ่มโรคที่เกิดกับระบบหัวใจและหลอด เลือดซึ่งเป็นสาเหตุการเสียชีวิตลำดับต้นของคนไทย ในแต่ละปีจะมีคนไทยเสียชีวิตจากโรคนี้ถึง 54,530 รายและมีแนวโน้มเพิ่มสูงขึ้นทุกปี โดยสามในสี่ของการเสียชีวิตด้วยโรคหัวใจและหลอดเลือดทั้งหมดเกิดจากโรค หลอดเลือดสมอง และโรคหัวใจขาดเลือด  ซึ่ง เกิดจากการที่หลอดเลือดตีบตันหรือขาดความยืดหยุ่น จากการสะสมของไขมัน โปรตีน และแร่ธาตุที่บริเวณ ผนังหลอดเลือด
<br><br>
ในปัจจุบันมีการตรวจคัดกรองสุขภาพโดยค้นหาปัจจัยเสี่ยงในการเกิดโรคดังกล่าวด้วยการประเมิน ความเสี่ยงโดยรวม ซึ่งเป็นการประเมินปัจจัยเสี่ยงหลายปัจจัยพร้อมๆ กันเพื่อทำนายโอกาสเกิดโรคภายในอนาคตข้างหน้า โดยปัจจัยเสี่ยงที่สำคัญและมีหลักฐานทางวิชาการว่าสัมพันธ์กับการเกิดโรคหัวใจและหลอดเลือด สามารถแบ่งได้เป็น 2 ประเภท ประเภทแรกคือ ปัจจัยเสี่ยงที่ปรับเปลี่ยนไม่ได้ เช่น อายุ เพศ ประวัติครอบครัว และ เชื้อชาติ ประเภทที่สองเป็นปัจจัยเสี่ยงที่ปรับเปลี่ยนได้ เช่น ความดันโลหิตสูง ระดับไขมันชนิดโคเลสเตอรอลรวมสูง ระดับไขมันชนิดเอชดีแอลต่างระดับน้ำตาลในเลือดสูง ภาวะอ้วนและ การสูบบุหรี่อีกทั้งการเป็นโรคร่วม ได้แก่ โรคไตเรื้อรัง โรคหัวใจเต้นผิดจังหวะชนิดโรคข้ออักเสบรูมาตอยด์ และภาวะหัวใจห้องล่างซ้ายโตก็เป็นปัจจัยเสี่ยงต่อการเกิดโรคหัวใจและหลอดเลือดได้ เช่นกัน

# **Analytic objective**
การทำโปรเจกต์ในครั้งนี้มีวัตถุประสงค์เพื่อนำช้อมูลเกี่ยวกับโรคหัวใจและหลอดเลือดมาศึกษาเพื่อหาความเสี่ยงในการเกิดโรคหัวใจและหลอดเลือดภายในระยะเวลา 10 ปี โดยใช้ความรู้ที่ได้เรียนจากวิชา CPE213 Data model มาประยุกต์ใช้

# **Data description**
Dataset เป็นข้อมูลที่เปิดเผยอยู่บน Kaggle https://www.kaggle.com/amanajmera1/framingham-heart-study-dataset เป็นข้อมูลที่ใช้ในการศึกษา ระบบหัวใจ และ หลอดเลือดของผู้อยู่อาศัยในเมือง Framingham, Massachusetts โดยมีข้อมูลกว่า 4,000 records and 15 attributes<br><br>

Male: เพศหญิงหรือชาย(ชาย = 1, หญิง = 0)<br>
Age: อายุ<br>
Education: ระดับการศึกษา(1 = Some High School, 2 = High School or GED, 3 = Some College or Vocational School, 4 = college)<br>
Current Smoker: สูบบุหรี่หรือไม่(1 = สูบ, 2 = ไม่สูบ)<br>
Cigs Per Day: จำนวนการสูบบุหรี่ต่อวัน<br>
BP Meds: ใช้ยาลดความดันเลือดหรือไม่(1 = ใช้ยาลดความดันเลือด, 0 = ไม่ใช้ยาลดความดันเลือด)<br>
Prevalent Stroke: เป็นโรคหลอดเลือดในสมองหรือไม่(1 = เป็น, 0 = ไม่เป็น)<br>
Prevalent Hyp: เป็นโรคความดันโลหิตสูงหรือไม่(1 = เป็น, 0 = ไม่เป็น)<br>
Diabetes: ป่วยเป็นโรคเบาหวานหรือไม่(1 = เป็น, 0 = ไม่เป็น)<br>
Tot Chol: ระดับคอเลสเตอรอลทั้งหมด (มิลลิกรัม/เดซิลิตร)<br>
Sys BP: ความดันโลหิตช่วงบน<br>
Dia BP: ความดันโลหิตช่วงล่าง<br>
BMI: ดัชนีมวลกาย<br>
Heart Rate: อัตราการเต้นของหัวใจ<br>
Glucose: ระดับน้ำตาล<br>
Ten Year CHD: ในระยะ 10 ปีที่จะเสี่ยงเป็นโรคหลอดเลือดหัวใจ(1 = ใช่, 0 = ไม่) (Target)<br>

# **Get started**

## Install Packages
"""

#@title 
install.packages("randomForest")
install.packages("tictoc")
install.packages("caret")
install.packages("caTools")
install.packages("e1071")
install.packages("xgboost")
install.packages("ROSE")
install.packages("MLmetrics")
install.packages("smotefamily")
install.packages("standardize")
install.packages("cowplot")

"""## Import Library"""

#@title 
library(tidyverse)
library(dplyr)
library(ggplot2)
library(randomForest)
library(caret)
library(tictoc)
library(caTools)
library(ROSE)
library(MLmetrics)
library(smotefamily)
library(standardize)
library(reshape2)
library(cowplot)

"""# **Get Data**
Download data จาก Goodle Drive
"""

system("gdown --id 1F0Z2_q4327V0Qz-8tEyFlNDYRX1Qaeoa")
framingham <- read.csv("framingham.csv")

"""# **Exploratory data analysis (EDA)**

ตรวจสอบข้อมูลเบื้องต้นด้วย head() เพื่อดูข้อมูล 5 แถวแรก
"""

head(framingham)

"""ตรวจสอบโครงสร้างของข้อมูลเบื้องต้นด้วย str()"""

### Looking at structure of the data
str(framingham)

"""ตรวจสอบความสัมพันธ์ของแต่ละ Feature กับ Target"""

#@title 
options(repr.plot.width = 15, repr.plot.height = 15)
#### Prepare data for Modeling ####
plot_data <- framingham
# duplicate target variable for building the model
plot_data  <- plot_data  %>% mutate(HD = TenYearCHD) 
# move target variables to column 1,2 
plot_data  <- plot_data  %>% select(HD, TenYearCHD, everything())
# rename columns for the header of data 
plot_data <- plot_data %>% rename("Heart Disease" = TenYearCHD,
                    Gender = male,
                    Age = age,
                    Education = education,
                    Smoker = currentSmoker)

plot_data$Gender = factor(plot_data$Gender, labels = c('Female', 'Male'))
plot_data$Smoker = factor(plot_data$Smoker, labels = c('Non Smoker', 'Smoker'))
plot_data$"Heart Disease" = factor(plot_data$"Heart Disease", labels = c('No', 'Yes'))
plot_data$prevalentStroke = factor(plot_data$prevalentStroke, labels = c('No', 'Yes'))
plot_data$prevalentHyp = factor(plot_data$prevalentHyp, labels = c('No', 'Yes'))
plot_data$diabetes = factor(plot_data$diabetes, labels = c('No', 'Yes'))
plot_data$BPMeds = factor(plot_data$BPMeds,labels = c("Not on Blood Pressure medications", "Blood Pressure medications"))
# replace missing values with numeric
plot_data$Education <- plot_data$Education %>% replace_na(5)
plot_data$Education = factor(plot_data$Education, 
                                labels = c("Some High School",
                                           "High School or GED",
                                           "Some College or Vocational School",
                                           "College", "Other"))
#### Visualization ####
#### 1 ####
x <- ggplot(plot_data, aes(factor(Smoker, labels = c("Not smoked", "Smoked")),fill = `Heart Disease`, color = `Heart Disease`)) +
  geom_bar(stat = "count", position = "dodge") +
  ggtitle("Current Smoke") + xlab("Current smoked")+
  theme_minimal()
#### 2 #### 
y <- ggplot(plot_data, aes(factor(Gender, labels = c("Female", "Male")),fill = `Heart Disease`, color = `Heart Disease`)) +
  geom_bar(stat = "count", position = "dodge")+
  ggtitle("Gender who have Heart disease") + xlab("Gender")+
  theme_minimal()
#### 3 ####
z <- ggplot(plot_data, aes(factor(BPMeds , labels = c("Not on Blood Pressure medications", "Blood Pressure medications")), 
                            fill = `Heart Disease`, color = `Heart Disease`)) + 
  geom_bar(stat = "count", position = "dodge") + 
  ggtitle("Blood Pressure Medication")+ xlab("BPMeds")+
  theme_minimal()
#### 4 ####
xx <- ggplot(plot_data, aes(prevalentStroke, fill = `Heart Disease`, color = `Heart Disease`)) + 
  geom_bar(stat = "count", position = "dodge") + 
  ggtitle("Prevelance of Stroke")+
  theme_minimal()
#### 5 ####
yy <- plot_data %>% filter(Education != "Other") %>%
  ggplot(aes(Education, fill = `Heart Disease`, color = `Heart Disease`)) + 
  geom_bar(stat = "count", position = "dodge") + 
  ggtitle("Education")+
  theme_minimal()
#### 6 ####
zz <- ggplot(plot_data, aes(prevalentHyp, fill = `Heart Disease`, color = `Heart Disease`)) + 
  geom_bar(stat = "count", position = "dodge") + 
  labs(title = "Prevelance of Hypertension") +  
  theme_minimal()

plot_grid(x,y,z,xx,yy,zz, ncol = 2, nrow = 3)

#@title 
#### 9 ####
options(repr.plot.width = 7, repr.plot.height = 7)
ggplot(plot_data, aes(factor(diabetes , labels = c("No", "Yes")), 
                       fill=`Heart Disease`, color = `Heart Disease`)) + 
  geom_bar(stat = "count", position = "dodge") + 
  ggtitle("Diabetes who have Heart disease")+ xlab("Diabetes")+
  theme_minimal()

#@title 
#### 7 ####
options(repr.plot.width = 10, repr.plot.height = 10)
plot_data$Age = as.numeric(plot_data$Age)
a <- ggplot(plot_data,aes(Age,color = ,fill=`Heart Disease`)) + 
  geom_density(lwd = 2, show.legend = T, alpha = 0.5) + 
  labs(title = "Age who have Heart disease")+
  theme_minimal()
#### 8 ####
b<- ggplot(plot_data,aes(cigsPerDay,color = ,fill=`Heart Disease`)) + 
  geom_density(lwd = 2, show.legend = T, alpha = 0.5) + 
  labs(title = "Cigarettes per day who have smoke",x = "Cigarettes per day")+
  theme_minimal()

plot_grid(a,b, ncol = 1, nrow = 2)

"""Boxplot เพื่อตรวจสอบ Outlier ของ Column age, cigsPerDay, totChol, sysBP, diaBP, BMI, heartRate และ glucose"""

options(repr.plot.width = 25, repr.plot.height = 10)
par(mfrow = c(1, 8), mar=c(1,1,1,1))
invisible(lapply(c(2, 5, 10, 11, 12, 13, 14, 15), function(i) boxplot(framingham[, i])))

"""ตรวจสอบจำนวนของข้อมูลว่าง (NA) พบว่ามีข้อมูลว่างที่ Column <br>
education  : 105 rows <br>
cigsPerDay : 31 rows <br>
BPMeds     : 53 rows <br>
totChol    : 50 rows <br>
BMI        : 19 rows <br>
heartRate  : 1 rows <br>
glucose    : 388 rows <br>
"""

print(sapply(framingham, function(x) sum(is.na(x))))

""" ตรวจสอบ Data Imbalance พบว่ามีข้อมูลที่ตอบ No มากกว่าตอบ Yes สูง"""

options(repr.plot.width=10, repr.plot.height=10)
ggplot(framingham, aes(as.factor(TenYearCHD))) + 
    geom_bar()

"""# **Data Preprocessing**
การเตรียมข้อมูลให้พร้อมนำไปใช้กับ Machine Learning Model

## Train Test Split
แบ่งข้อมูลออกเป็น 2 ส่วน คือ <br>
Train ใช้ในการ Train Machine Learning Model <br>
Test ใช้ในการ Test ประสิทธิภาพของ Model <br>
โดยแบ่งเป็น Train 80% และ Test 20%
"""

### Randomly spliting the data into train and test sets
set.seed(1000)
split <- sample.split(framingham$TenYearCHD, SplitRatio = 0.80)
train <- subset(framingham, split==TRUE)
test <- subset(framingham, split==FALSE)

"""## Outlier Removal
กำจัด Outlier ใน Train set
"""

outlierKD <- function(dt, var) {
     var_name <- eval(sym(var),eval(dt))
     na1 <- sum(is.na(var_name))
     m1 <- mean(var_name, na.rm = T)
     par(mfrow=c(2, 2), oma=c(0,0,3,0))
     boxplot(var_name, main="With outliers")
     hist(var_name, main="With outliers", xlab=NA, ylab=NA)
     outlier <- boxplot.stats(var_name)$out
     mo <- mean(outlier)
     var_name <- ifelse(var_name %in% outlier, NA, var_name)
     boxplot(var_name, main="Without outliers")
     hist(var_name, main="Without outliers", xlab=NA, ylab=NA)
     title("Outlier Check", outer=TRUE)
     na2 <- sum(is.na(var_name))
     cat("Outliers identified:", na2 - na1, "n")
     cat("Propotion (%) of outliers:", round((na2 - na1) / sum(!is.na(var_name))*100, 1), "n")
     cat("Mean of the outliers:", round(mo, 2), "n")
     m2 <- mean(var_name, na.rm = T)
     cat("Mean without removing outliers:", round(m1, 2), "n")
     cat("Mean if we remove outliers:", round(m2, 2), "n")

     dt[as.character(sym(var))] <- invisible(var_name)
     assign(as.character(as.list(match.call())$dt), dt, envir = .GlobalEnv)
     cat("Outliers successfully removed", "n")
     return(invisible(dt))

}

options(repr.plot.width = 10, repr.plot.height = 10)
for (i in c( 5, 10, 11, 12, 13, 14, 15)){
  outlierKD(train, names(train)[i])
  dev.off()
}

"""จะพบว่าเพื่อ Plot Boxplot จะมีค่า Outlier ที่ลดลง"""

options(repr.plot.width = 25, repr.plot.height = 10)
par(mfrow = c(1, 8), mar=c(1,1,1,1))
invisible(lapply(c(2, 5, 10, 11, 12, 13, 14, 15), function(i) boxplot(train[, i])))

"""## Dealing with NA

Plot Distribution ระหว่าง แต่ละ Column กับ Target เพื่อเปรียบเทียบ Distribution ก่อน และ หลัง Fill NA
"""

#@title 
options(repr.plot.width=15, repr.plot.height=15)
fh <- data.frame(dummyvar=1:nrow(train),sapply(1:length(train),rnorm,n=nrow(train)))
colnames(fh)[-1] = names(train)
var_to_plot = c("education","cigsPerDay","BPMeds","totChol","BMI", "heartRate", "glucose")
dummyvar = "dummyvar"
ggplot(pivot_longer(fh[,c(var_to_plot,dummyvar)],-dummyvar), aes(x=value)) +
  geom_histogram(aes(y=..density..), bins = 50,  colour = "black", fill = "white") +
    geom_density(aes(y=..density..), alpha = .2, fill = "#FF6666") + 
      facet_wrap(~name)

"""Fill NA ด้วยค่า Median และ แสดงผลจำนวน NA ที่พบในข้อมูล"""

# framingham[is.na(framingham)] <- 0
# print(sapply(framingham, function(x) sum(is.na(x))))

train$education[is.na(train$education)] <- median(train$education,na.rm=TRUE)
train$cigsPerDay [is.na(train$cigsPerDay )] <- median(train$cigsPerDay ,na.rm=TRUE)
train$BPMeds[is.na(train$BPMeds)] <- median(train$BPMeds,na.rm=TRUE)
train$totChol[is.na(train$totChol)] <- median(train$totChol,na.rm=TRUE)
train$BMI[is.na(train$BMI)] <- median(train$BMI,na.rm=TRUE)
train$heartRate[is.na(train$heartRate)] <- median(train$heartRate,na.rm=TRUE)
train$glucose[is.na(train$glucose)] <- median(train$glucose,na.rm=TRUE)

test$education[is.na(test$education)] <- median(train$education,na.rm=TRUE)
test$cigsPerDay [is.na(test$cigsPerDay )] <- median(train$cigsPerDay ,na.rm=TRUE)
test$BPMeds[is.na(test$BPMeds)] <- median(train$BPMeds,na.rm=TRUE)
test$totChol[is.na(test$totChol)] <- median(train$totChol,na.rm=TRUE)
test$BMI[is.na(test$BMI)] <- median(train$BMI,na.rm=TRUE)
test$heartRate[is.na(test$heartRate)] <- median(train$heartRate,na.rm=TRUE)
test$glucose[is.na(test$glucose)] <- median(train$glucose,na.rm=TRUE)


train$sysBP[is.na(train$sysBP)] <- median(train$sysBP,na.rm=TRUE)
train$diaBP[is.na(train$diaBP)] <- median(train$diaBP,na.rm=TRUE)

test$sysBP[is.na(test$sysBP)] <- median(train$sysBP,na.rm=TRUE)
test$diaBP[is.na(test$diaBP)] <- median(train$diaBP,na.rm=TRUE)

print(sapply(train, function(x) sum(is.na(x))))

"""Plot Distribution หลังการ Fill NA พบว่ามี Distribution ที่ไม่แตกต่างจากเดิมมากนัก"""

#@title 
options(repr.plot.width=15, repr.plot.height=15)
fh <- data.frame(dummyvar=1:nrow(train),sapply(1:length(train),rnorm,n=nrow(train)))
colnames(fh)[-1] = names(train)
var_to_plot = c("education","cigsPerDay","BPMeds","totChol","BMI", "heartRate", "glucose")
dummyvar = "dummyvar"
ggplot(pivot_longer(fh[,c(var_to_plot,dummyvar)],-dummyvar), aes(x=value)) +
  geom_histogram(aes(y=..density..), bins = 50,  colour = "black", fill = "white") +
    geom_density(aes(y=..density..), alpha = .2, fill = "#FF6666") + 
      facet_wrap(~name)

"""## Over Sampling with Synthetic Minority Oversampling TEchnique (SMOTE)
จัดการกับ Imbalance Data ด้วยการทำ Over Sampling with SMOTE <br>
โดยมีค่า Parameters K = 4, dup_size = 4
"""

### Over Sampling with SMOTE
train_balanced <- SMOTE(X = train, target = train$TenYearCHD,K = 4, dup_size = 4)$data
train_balanced <- train_balanced[,-length(train_balanced)]
print(paste0("Add data: ", nrow(train_balanced) - nrow(train), " rows"))

train_balanced$TenYearCHD <- as.factor(train_balanced$TenYearCHD)
levels(train_balanced$TenYearCHD) <- c("no", "yes")

options(repr.plot.width=10, repr.plot.height=10)
ggplot(train_balanced, aes(TenYearCHD)) + 
  geom_bar()

"""## Normaliztion
ทำการ Normalization ด้วย Standardization

Range ของข้อมูลก่อน Standardization
"""

summary(train_balanced)

train_balanced_scaled <- train_balanced
test_scaled <- test

for (c in names(train_balanced)){
  if (c != "TenYearCHD"){
    train_balanced_scaled[c] <- scale(train_balanced[c])
    test_scaled[c] <- scale(test[c], mean(train_balanced[[c]]), sd(train_balanced[[c]]))
  }
}
test_scaled$TenYearCHD <- as.factor(test_scaled$TenYearCHD)
levels(test_scaled$TenYearCHD) <- c("no", "yes")

"""Range ของข้อมูลหลัง Standardization"""

summary(train_balanced_scaled)

"""## Feature Selection
ทำการเลือก Feature ที่มีความสำคัญมากกว่า 0.4 มาใช้ในการ Train Machine Learning Model ด้วย Feature Importance ที่ได้จาก XGBoost Model <br>
พบว่ามี Feature ที่มี Feature Importance เกิน 0.4 ดังนี้ education, male,  age, และ prevalentHyp
"""

### XGBoost Model
xgb <- train(TenYearCHD ~ ., data = train_balanced_scaled, 
             method = "xgbTree", verbose = FALSE)
caret_imp <- varImp(xgb)
plot(caret_imp)

caret_imp

train_balanced_scaled_fi <- train_balanced_scaled[c('education', 'male', 'prevalentHyp', 'age', 'TenYearCHD')]
test_scaled_fi <- test_scaled[c('education', 'male', 'prevalentHyp', 'age', 'TenYearCHD')]

"""# **Train Model**

## Cross Validation
กำหนดการทำ Crossvalidation ในการ Train เป็น 5-Repeated 10-Fold Cross Validation With F1-score Matric
"""

### 5-Repeated 10-Fold Cross Validation 
f1 <- function(data, lev = NULL, model = NULL) {
  f1_val <- F1_Score(y_pred = data$pred, y_true = data$obs, positive = "yes")
  c(F1 = f1_val)
}

fitControl <- trainControl(method = "repeatedcv", number = 10, repeats = 5, 
                          summaryFunction = f1, classProbs = TRUE)

"""## Logistic Regression Model"""

### Logistic Regression Model
tic()
glm_model <- train(TenYearCHD ~ ., data = train_balanced_scaled_fi, method = "glm")
toc()

glm_model

### Confusion matrix with threshold of 0.5
prediction_glm <- predict(glm_model,type="prob", train_balanced_scaled_fi)
pred <- as.factor(as.numeric(prediction_glm[2] > 0.6))
levels(pred) <- c("no", "yes")
t <- table(train_balanced_scaled_fi$TenYearCHD, pred)
confusionMatrix(t, positive = "yes")

# Metric Fucntion
measurement <- function (t) {
  me_list <- c()
  i <- 1
  for (a in 1:4){
    if (is.na(t[a])) {                                                                                                                                                                                                                                                                                                                                                                                                                                                      
      me_list[i] <- 0
    } else {
      me_list[i] <- t[a]
    }
    i<-i+1
  }

  TP <- me_list[4]
  TN <- me_list[1]
  FP <- me_list[3]
  FN <- me_list[2]

  acc <- (TP+TN)/(TP+TN+FP+FN)
  if (TP+FP == 0) {
    ra <- 1
  } else {
    ra <- TP+FP
  }
  precision <- (TP)/(ra)
  if (TP+FN == 0) {
    rs <- 1
  } else {
    rs <- TP+FN
  }
  recall_score <- (TP)/(rs)
  f1_score <- 2*((precision*recall_score)/(precision+recall_score))
  print(paste0("Accuracy : ", acc))
  print(paste0("Precision: ", precision))
  print(paste0("Recall   : ", recall_score))
  print(paste0("F1-Score : ", f1_score))
}

measurement(t)

"""## Neural Network Model"""

### Neural Network Model
tic()
nnet_model <- train(TenYearCHD ~ ., data = train_balanced_scaled_fi, method = "nnet", 
                    trControl = fitControl, verbose = FALSE, metric = "F1", maxit=1000)
toc()

nnet_model

prediction_nnet <- predict(nnet_model,type="prob", train_balanced_scaled_fi)
pred <- as.factor(as.numeric(prediction_nnet[2] > 0.4))
levels(pred) <- c("no", "yes")
t <- table(train_balanced_scaled_fi$TenYearCHD, pred)
confusionMatrix(t, positive = "yes")

measurement(t)

"""## Extreme Gradient Boosting (XGBoost) Model"""

### XGBoost Model
tic()
xgb <- train(TenYearCHD ~ ., data = train_balanced_scaled_fi, method = "xgbTree", 
             trControl = fitControl, verbose = FALSE, metric = "F1")
toc()

xgb

### Confusion matrix with threshold of 0.5
prediction_xgb <- predict(xgb,type="prob", train_balanced_scaled_fi)
pred <- as.factor(as.numeric(prediction_xgb[2] > 0.2))
levels(pred) <- c("no", "yes")
t <- table(train_balanced_scaled_fi$TenYearCHD, pred)
confusionMatrix(t, , positive = "yes")

measurement(t)

"""## Stacking Model 
นำ Models Logistic Regression, Neural Network และ XGBoost มา Stacking และทำ Hard Voting 
"""

### Stacking Model 
combPred <- ((prediction_glm[2] > 0.6) + (prediction_nnet[2] > 0.4) + (prediction_xgb[2] > 0.2 )) / 3

### Confusion matrix with threshold of 0.5
pred <- as.factor(as.numeric(combPred > 0.5))
levels(pred) <- c("no", "yes")
t <- table(train_balanced_scaled_fi$TenYearCHD, pred)
confusionMatrix(t, positive = "yes")

measurement(t)

"""# Evaluate
ทดสอบประสิทธิภาพของ Model กับ Testset ด้วย Confusion Matrix
"""

test_xgb <- predict(xgb, type="prob", test_scaled_fi)[2] > 0.3
row.names(test_xgb) <- NULL
test_nnet <- predict(nnet_model,type="prob", test_scaled_fi)[2] > 0.5
row.names(test_nnet) <- NULL 
test_glm <- predict(glm_model,type="prob", test_scaled_fi)[2] > 0.3
row.names(test_glm) <- NULL
combPred <- (test_xgb + test_nnet + test_glm ) / 3

### Confusion matrix with threshold of 0.5
pred <- as.factor(as.numeric(combPred > 0.5))
levels(pred) <- c("no", "yes")
t <- table(test_scaled_fi$TenYearCHD, pred)
confusionMatrix(t, positive = "yes")

measurement(t)

"""# **Discussion and Conclusion**
ใน Project นี้ กลุ่มของดราได้ทำการศึกษาเพื่อหาความเสี่ยงในการเกิดโรคหัวใจและหลอดเลือดภายในระยะเวลา 10 ปีด้วยช้อมูลเกี่ยวกับโรคหัวใจและหลอดเลือด  ซึ่งประกอบไปด้วยกระบวนการทาง Data science 5 ขั้นตอนด้วยกัน Get data, EDA, Data preprocessing, Train model และ Evaluate ในขั้นตอนของการ EDA กลุ่มเราได้ทำการตรวจสอบข้อมูลและพบว่ามีปัญหา 3 ปัญหาด้วยกัน คือ 
- Outlier : พบว่าข้อมูลมี Outlier 
- NaN : ข้อมูลมี NaN
- Data imbalance : Label ของข้อมูล มีจำนวนระหว่างคำตอบ + และคำตอบ - ต่างกันมาก<br>

ดังนั้นในขั้นตอน Data preprocessing จึงได้มีการแก้ปัญหาที่กล่าวมาข้างต้นด้วย
- Outlier removal : ทำการลบข้อมูลที่เป็น Outlier ออก
- Fill NaN : ทำการแทนนค่าที่เป็น NaN ด้วยค่า Median
- SMOTE : ทำ Over sampling เพื่อเพิ่มข้อมูลที่มีจำนวนน้อย

นอกจากนี้ยังมีการทำเพิ่มประสิทธิภาพของ Model ด้วย
- Train test split : แบ่ง Trainset และ Testset ออกจากกัน
- Normalization : ทำให้ข้อมูลอยู่บน Range เดียวกันด้วย Standard scaler
- Feature selection : ทำการตัดข้อมูลบาง Feature ที่มีความสำคัญน้อยออกด้วย Feature importance จาก XGBoost

ในขั้นตอน Train model กลุ่มของเราออกแบบโดยใช้ Ensemble method ด้วย 3 Models ด้วยกันคือ Logistic regression, Neural network และ XGBoost เพื่อให้การทำนายมีความแม่นยำมากขึ้น และ นำผลลัพท์จาก 3 Models มาทำ Hard Voting เพื่อให้ได้ Ensemble output สุดท้ายออกมา <br>
ในการ Train ยังมีการทำ Cross validation ด้วย F1-score metric เพื่อ ให้ผลลัพท์ดีขึ้นด้วยปริมาณข้อมูลเท่าเดิม 

สุดท้ายในการทดสอบ Model เราได้ใช้ Confusion metrix เพื่อทดสอบประสิทธิภาพ เพื่อป้องกันปัญหาที่จะเกิดขึ้นจก Skewed data 

ผลลัพท์จากกระบวนการข้างต้น ได้ผลลัพท์ Precision 0.32, Recall 0.45 และ F1-score ที่ 0.38 ซึ่งยังเป็นผลลัพท์ที่ยังไม่สามารถนำไปใช้งานจริงกับโรงพยาบาลได้

ข้อเสนอแนะ คิดว่าเราสามารถเพิ่มความถูกต้องของ Model ได้ในกรณีที่มีข้อมูลมากกว่านี้จากการสำรวจกลุ่มผู้ป่วยโรคหัวใจในเมืองอื่น และ เปลี่ยน Model ให้มีความซับซ้อนมากขึ้น



"""
