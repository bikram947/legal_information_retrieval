from flask import Flask,render_template,request
import matplotlib.pyplot as plt
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
@app.route('/states',methods = ['POST', 'GET'])
def states():

    top10=[]

    types=-1
    if request.method=='POST':
        state=request.form['state']
        d={'Advocates involved':'Advocates involved','Parties involved':'Persons involved','Analytics of Frequent Complainants':'Complainant', 'Analytics of Frequent Respondents':'Respondent', 'Analytics of Complainant Advocates':'Complainant Advocate', 'Analytics of Respondent Advocates':'Respondent Advocate', 'Analytics of shortest running cases':'Shortest running cases', 'Analytics of longest running cases':'Longest running cases'}
        analysis_type=d[request.form['typestat']]

        df_state = pd.read_csv('./datasets/'+state+'_'+analysis_type+'.csv')
        #print(df_state)
        df_state=df_state.iloc[:,1:]
        #print(df_state)
        if(df_state.shape[0]==0):
            types=-2
        elif analysis_type =="Longest running cases" or analysis_type =="Shortest running cases":
            top10 = df_state.values.tolist()
            print(top10)
            com = []
            cases=[]
            for i in range(len(top10)):
                com.append(top10[i][0])
                cases.append(top10[i][2])
            data = {analysis_type: com,
                    'Duration': cases
                }
            df = pd.DataFrame(data,columns=[analysis_type,'Duration'])
            fig=df.plot(x =analysis_type, y='Duration', kind = 'bar',title=request.form['typestat']+" for "+state).get_figure()
            fig.savefig('./static/output.png',bbox_inches='tight')
            types=1
            top10.insert(0,['Case No','Duration'])
        else:
            top10= df_state.values.tolist()
            print(top10)
            com = []
            cases=[]
            for i in range(len(top10)):
                com.append(top10[i][0])
                cases.append(top10[i][1])
                #print(com)
                #print(cases)
            if(analysis_type=='Persons involved'):
                analysis_type='Parties invloved'
            data = {analysis_type: com,
                        'No. of cases': cases
                    }
                #print(data)
            df = pd.DataFrame(data,columns=[analysis_type,'No. of cases'])
            fig=df.plot(x =analysis_type, y='No. of cases', kind = 'bar',title=request.form['typestat']+" for "+state).get_figure()
            fig.savefig('./static/output.png',bbox_inches='tight')
            types=1
            top10.insert(0,[analysis_type,'No. of cases'])


    return render_template('states.html',queryOutput=top10,types=types)


@app.route('/india',methods = ['POST', 'GET'])
def india():
    top10=[]

    types=-1
    if request.method=='POST':
        state='India'
        d={'Advocates involved':'Advocates involved','Parties involved':'Persons involved','Analytics of Frequent Complainants':'Complainant', 'Analytics of Frequent Respondents':'Respondent', 'Analytics of Complainant Advocates':'Complainant Advocate', 'Analytics of Respondent Advocates':'Respondent Advocate', 'Analytics of shortest running cases':'Shortest running cases', 'Analytics of longest running cases':'Longest running cases'}
        analysis_type=d[request.form['typestat']]

        df_state = pd.read_csv('./datasets/'+state+'_'+analysis_type+'.csv')
        #print(df_state)
        df_state=df_state.iloc[:,1:]
        #print(df_state)
        if(df_state.shape[0]==0):
            types=-2
        elif analysis_type =="Longest running cases" or analysis_type =="Shortest running cases":
            top10 = df_state.values.tolist()
            print(top10)
            com = []
            cases=[]
            for i in range(len(top10)):
                com.append(top10[i][0])
                cases.append(top10[i][2])
            data = {analysis_type: com,
                    'Duration': cases
                }
            df = pd.DataFrame(data,columns=[analysis_type,'Duration'])
            fig=df.plot(x =analysis_type, y='Duration', kind = 'bar',title=request.form['typestat']+" for "+state).get_figure()
            fig.savefig('./static/output.png',bbox_inches='tight')
            types=1
            top10.insert(0,['Case No','Duration'])
        else:
            top10= df_state.values.tolist()
            print(top10)
            com = []
            cases=[]
            for i in range(len(top10)):
                com.append(top10[i][0])
                cases.append(top10[i][1])
                #print(com)
                #print(cases)
            if(analysis_type=='Persons involved'):
                analysis_type='Parties invloved'
            data = {analysis_type: com,
                        'No. of cases': cases
                    }
                #print(data)
            df = pd.DataFrame(data,columns=[analysis_type,'No. of cases'])
            fig=df.plot(x =analysis_type, y='No. of cases', kind = 'bar',title=request.form['typestat']+" for "+state).get_figure()
            fig.savefig('./static/output.png',bbox_inches='tight')
            types=1
            top10.insert(0,[analysis_type,'No. of cases'])


    return render_template('india.html',queryOutput=top10,types=types)


if __name__ == "__main__":
    app.run(host="localhost", port=5046)