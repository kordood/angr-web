import angr
import networkx as nx
from matplotlib import pyplot as plt


class Manager:

    def __init__(self, binary, cfg_emulated=False, **kwargs):
        self.binary = binary
        self.project = angr.Project(binary, **kwargs)
        self.cfg_emulated= cfg_emulated
        self.cfg = self.generate_cfg()
        self.callgraph = None
        self.cfg_visual = None
        self.callgraph_visual = None

    def generate_cfg(self):
        cfg = self.project.analyses.CFG_Emulated() if self.cfg_emulated else self.project.analyses.CFGFast()
        return cfg

    def visualize_cfg(self, **kwargs):
        if self.cfg is None:
            self.cfg = self.generate_cfg()

        self.draw_graph(self.cfg, **kwargs)

    def visualize_callgraph(self, **kwargs):
        if self.cfg is None:
            self.cfg = self.generate_cfg()

        self.callgraph = self.cfg.kb.callgraph

        self.draw_graph(self.callgraph, **kwargs)

    def draw_graph(self, G, format='PNG', figsize=(80, 10), dpi=100, **kwargs):
        for key, value in kwargs.items():
            if key == "G":
                G = value
            elif key == "format":
                format = value
            elif key == "figsize":
                figsize = value
            elif key == "dpi":
                dpi = value

        fig = plt.figure(figsize=figsize, dpi=dpi, facecolor='w', edgecolor='k')
        nx.draw(G, pos=nx.drawing.nx_agraph.graphviz_layout(G, prog='dot'), with_labels=True)

        plt.savefig("graph.png", format=format)
