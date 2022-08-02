"""Model fitting and inference."""
import statsmodels.api as sm


class LogisticRegression:
    def __init__(self, intercept=True):
        self.model = None
        self.intercept = intercept
        pass

    def fit(self, X, y):
        if self.intercept:
            X = sm.add_constant(X)
        self.model = sm.Logit(exog=X, endog=y).fit()
        return

    def summary(self):
        return self.model.summary()
