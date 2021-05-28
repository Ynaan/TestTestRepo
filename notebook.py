# Databricks notebook source
1 + 1 222  4544

# COMMAND ----------

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])

# COMMAND ----------

# MAGIC %sh ls /tmp

# COMMAND ----------

display(spark.range(1, 100000))

# COMMAND ----------

import pandas as pd
t = [["44", "444", "7890"]]
for i in range(1, 1001):
  t.append(['x' * 10, '55555', '11111'])
df = pd.DataFrame(t)
display(df)

# COMMAND ----------

# MAGIC %sh cat > /dbfs/test.csv <<EOF
# MAGIC a,1
# MAGIC b,2
# MAGIC EOF

# COMMAND ----------

# MAGIC %scala
# MAGIC println("HI")
# MAGIC System.out.println("HELLO")
# MAGIC System.err.println("GOODBYE")
# MAGIC Console.err.println("END")

# COMMAND ----------

# MAGIC %r
# MAGIC library(ggplot2)
# MAGIC display(diamonds)

# COMMAND ----------

displayHTML("<script>console.log(window.parent.body);</script>")

# COMMAND ----------

displayHTML("<script>missing</script>")

# COMMAND ----------

# MAGIC %scala 
# MAGIC val map = Map("good" -> "good")
# MAGIC print(map.toString)

# COMMAND ----------

# MAGIC %md ### 1 + 1

# COMMAND ----------

lll