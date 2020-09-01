import pandas as pd
import random


def standard(listt):
    return str(listt).replace(" ", "").replace("[", "").replace("]", "")

def make_csv(df,student_list,filename,path,train=True):
  suffix= '_train1.csv' if train else '_valid1.csv'
  f=open(path+filename+suffix,"w+")
  for student in student_list:
    questions=[]
    answers=[]
    cond=df['user_id'] == student
    temp_df=df[cond]
    temp_df.head()
    #print(len(temp_df))
    questions=temp_df['problem_id'].tolist()
    answers=temp_df['correct'].tolist()
    no_questions=len(questions)
    f.write(str(no_questions)+'\n')
    f.write(standard(questions)+'\n')
    f.write(standard(answers)+'\n')

  f.close()

def create(filename,path):
    #Udio training seta od cijelog dataseta
    TRAIN_PART=0.7

    df=pd.read_csv(path,index_col=None,delimiter='\t')

    students=df.user_id.unique()
    random.shuffle(students)

    train_size=round(len(students)*TRAIN_PART)
    #print(train_size)
    train_students=students[:train_size]
    #print(len(train_students))
    validation_students=students[train_size:-1]
    #print(len(validation_students))
    make_csv(df,train_students,filename,path)
    make_csv(df,validation_students,filename,path,False)