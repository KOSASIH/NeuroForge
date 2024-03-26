import shap
import lime
import matplotlib.pyplot as plt

def explain_model(model, data, target_names):
    """
    Explain the decision-making process of a machine learning model using SHAP and LIME.
    """
    # Explain model using SHAP
    explainer_shap = shap.TreeExplainer(model)
    shap_values = explainer_shap.shap_values(data)
    shap.summary_plot(shap_values, data, plot_type="bar", feature_names=target_names)
    plt.show()

    # Explain model using LIME
    explainer_lime = lime.lime_tabular.LimeTabularExplainer(data, feature_names=target_names, class_names=target_names)
    lime_explanation = explainer_lime.explain_instance(data, model.predict, num_features=len(target_names))
    lime.lime_tabular.lime_text(lime_explanation)
