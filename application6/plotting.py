import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool, ColumnDataSource



df=pandas.read_csv("time.csv")

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds=ColumnDataSource(df)

p=figure(x_axis_type="datetime",height=500, width=500, title="Motion Graph",sizing_mode="scale_width")

p.yaxis.minor_tick_line_color=None
# p.ygrid[0].ticker.desired_num_ticks=1



hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

q=p.quad(left="Start_string",right="End_string",bottom=0,top=1,color="green",source=cds)

output_file("graph.html")
show(p)


