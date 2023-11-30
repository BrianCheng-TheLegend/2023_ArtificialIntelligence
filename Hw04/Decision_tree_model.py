from sklearn.tree import export_graphviz

# visualize the model, export graphviz 
export_graphviz(model, out_file='mushrooms.dot',
                feature_names=['size', 'length'],
                class_names=model.classes_)