import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data preprocessing for this dataset
class Data_preprocessing:
    def __init__(self,file_name):
        self.original_data = pd.read_csv(file_name)
        self.data=self.original_data.copy()
        self.Change_head(self.data)

    ### remove the space in str to aviod error message
    def Change_head(self,data):
        new_colums ={ title: title.replace(' ','')for title in data.head()}
        data.rename(columns=new_colums,inplace=True)
    

# Decision tree
class Decision_tree:
    def __init__(self,file_name):
        self.data=Data_preprocessing(file_name)
        # self.Categorical_options(self.data.data.head())

    ### calculate Entropy
    def Entropy(self,column):
        p=column.value_counts()/column.shape[0]
        entropy=np.sum(-p*np.log2(p+1e-9))
        return entropy
    ### calculate variance
    def variance(self,column):
        if(len(column)==1):
            return 0
        else:
            return column.var()
        
    ## calculate Information Gain by entropy
    # def Information_Gain(self,column,mask,variance=variance,function=Entropy): ## general form
    def Information_Gain(self,column,mask):
        a = sum(mask)
        b = mask.shape[0] - a
        
        if(a == 0 or b ==0): 
            ig = 0
        else:
            if column.dtypes != 'O':
                ig = self.variance(column) - (a/(a+b)* self.variance(column[mask])) - (b/(a+b)*self.variance(column[-mask]))
            else:
                ig = self.Entropy(column)-a/(a+b)*self.Entropy(column[mask])-b/(a+b)*self.Entropy(column[-mask])
        return ig

    ### Combination Generator
    def Combination_Generator(self,data,cur_index,cur_combi,all_combi):
        combination_with_current = cur_combi + [data[cur_index]]
        if cur_index == len(data):
            return combination_with_current
        all_combi.append(combination_with_current)

        # Recur with the current element included
        self.Combination_Generator(data,cur_index + 1, combination_with_current, all_combi)
        
        # Recur without the current element
        self.Combination_Generator(data,cur_index + 1, cur_combi, all_combi)

    ## 
    def Categorical_options(self,data):
        data=data.unique()
        Cat_op=[]
        self.Combination_Generator(0,[],Cat_op)
        return Cat_op[1:-1]
    
##################Source:https://anderfernandez.com/en/blog/code-decision-tree-python-from-scratch/
    def max_information_gain_split(self,x, y):
        split_value = []
        ig = [] 

        numeric_variable = True if x.dtypes != 'O' else False

        # Create options according to variable type
        if numeric_variable:
            options = x.sort_values().unique()[1:]
        else: 
            options = self.Categorical_options(x)

        # Calculate ig for all values
        for val in options:
            mask =   x < val if numeric_variable else x.isin(val)
            val_ig = self.Information_Gain(y, mask)
            # Append results
            ig.append(val_ig)
            split_value.append(val)

        # Check if there are more than 1 results if not, return False
        if len(ig) == 0:
            return(None,None,None, False)

        else:
        # Get results with highest IG
            best_ig = max(ig)
            best_ig_index = ig.index(best_ig)
            best_split = split_value[best_ig_index]
            return(best_ig,best_split,numeric_variable, True)
    def get_best_split(self,y, data):
        masks = data.drop(y, axis= 1).apply(self.max_information_gain_split, y = data[y])
        if sum(masks.loc[3,:]) == 0:
            return(None, None, None, None)

        else:
            # Get only masks that can be splitted
            masks = masks.loc[:,masks.loc[3,:]]

            # Get the results for split with highest IG
            split_variable = masks.iloc[0].astype(np.float32).idxmax()
            #split_valid = masks[split_variable][]
            split_value = masks[split_variable][1] 
            split_ig = masks[split_variable][0]
            split_numeric = masks[split_variable][2]

            return(split_variable, split_value, split_ig, split_numeric)
    def make_split(self,variable, value, data, is_numeric):
        if is_numeric:
            data_1 = data[data[variable] < value]
            data_2 = data[(data[variable] < value) == False]
        else:
            data_1 = data[data[variable].isin(value)]
            data_2 = data[(data[variable].isin(value)) == False]
        return(data_1,data_2)
    def make_prediction(self,data, target_factor):
        # Make predictions
        if target_factor:
            pred = data.value_counts().idxmax()
        else:
            pred = data.mean()
        return pred
    def train_tree(self,data,y, target_factor, max_depth = None,min_samples_split = None, min_information_gain = 1e-20, counter=0, max_categories = 20):
    # Check that max_categories is fulfilled
        if counter==0:
            types = data.dtypes
            check_columns = types[types == "object"].index
            for column in check_columns:
                var_length = len(data[column].value_counts()) 
                if var_length > max_categories:
                    raise ValueError('The variable ' + column + ' has '+ str(var_length) + ' unique values, which is more than the accepted ones: ' +  str(max_categories))

        # Check for depth conditions
        if max_depth == None:
            depth_cond = True

        else:
            if counter < max_depth:
                depth_cond = True

            else:
                depth_cond = False

        # Check for sample conditions
        if min_samples_split == None:
            sample_cond = True

        else:
            if data.shape[0] > min_samples_split:
                sample_cond = True

            else:
                sample_cond = False

        # Check for ig condition
        if depth_cond & sample_cond:

            var,val,ig,var_type = self.get_best_split(y, data)

            # If ig condition is fulfilled, make split 
            if ig is not None and ig >= min_information_gain:

                counter += 1

                left,right = self.make_split(var, val, data,var_type)

                # Instantiate sub-tree
                split_type = "<=" if var_type else "in"
                question =   "{} {}  {}".format(var,split_type,val)
                # question = "\n" + counter*" " + "|->" + var + " " + split_type + " " + str(val) 
                subtree = {question: []}


                # Find answers (recursion)
                yes_answer = self.train_tree(left,y, target_factor, max_depth,min_samples_split,min_information_gain, counter)

                no_answer = self.train_tree(right,y, target_factor, max_depth,min_samples_split,min_information_gain, counter)

                if yes_answer == no_answer:
                    subtree = yes_answer

                else:
                    subtree[question].append(yes_answer)
                    subtree[question].append(no_answer)

            # If it doesn't match IG condition, make prediction
            else:
                pred = self.make_prediction(data[y],target_factor)
                return pred

        # Drop dataset if doesn't match depth or sample conditions
        else:
            pred = self.make_prediction(data[y],target_factor)
            return pred

        return subtree
# train

    # predict
    def clasificar_datos(self,observacion, arbol):
        question = list(arbol.keys())[0] 
        if question.split()[1] == '<=':
            if observacion[question.split()[0]] <= float(question.split()[2]):
                answer = arbol[question][0]
            else:
                answer = arbol[question][1]

        else:
            if observacion[question.split()[0]][i] in (question.split()[2]):
                answer = arbol[question][0]
            else:
                answer = arbol[question][1]

        # If the answer is not a dictionary
        if not isinstance(answer, dict):
            return answer
        else:
            residual_tree = answer
            return self.clasificar_datos(observacion, answer)
    # save/load
        # import pickle

        # with open("decision_results.pkl", "wb") as tf:
        #     pickle.dump(dec, tf)
######################################################################################################







if __name__ == '__main__':
    pre_data=Decision_tree('train.csv')
    max_depth = 4
    min_samples_split = 20
    min_information_gain  = 1e-5
    dec=pre_data.train_tree(pre_data.data.data,'fake',True,max_depth=max_depth,min_samples_split=min_samples_split,min_information_gain=min_information_gain)
    print(dec)
    test_data=Data_preprocessing('test.csv')
    prediction = []
    num_obs = len(test_data.data)
    # num_obs=3

    for i in range(num_obs):
        # print(test_data.data.iloc[i,:])
        pred = pre_data.clasificar_datos(test_data.data.iloc[i,:], dec)
        prediction.append(pred)

    print("Predictions: ",prediction,
    "\n\nReal values:", test_data.data.fake[:num_obs].to_numpy())
    a=0
    for i in range(num_obs):
        a+=np.abs(prediction[i]-test_data.data.fake[:num_obs].to_numpy()[i])
    print("accuracy",((num_obs-a)/num_obs))