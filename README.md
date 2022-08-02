# simplr
Simple Logistic Regression in Python


## Why?

I like the `scikit-learn` api for fitting models but `statsmodels` provides confidence intervals/ inference output. So we wrap `statsmodels` in a class and call it like we would `scikit-learn`'s `LogisticRegression`.


## Usage

```python
from simplr.model import LogisticRegression

model = LogisticRegression()
model.fit(X, y)
model.summary()
```
