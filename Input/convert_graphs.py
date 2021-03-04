#!/usr/bin/env python

import sys, os, glob

sys.path.insert(0, "/Users/teague/ResearchWorkspace/dqva-and-circuit-cutting")

from utils import helper_funcs
from utils import graph_funcs

if __name__ == '__main__':
    graph_dir = sys.argv[1]
    print('Converting graphs from:\n\t', graph_dir)

    all_graphs = glob.glob(graph_dir + '/*')
    print(len(all_graphs))

    for graph in all_graphs:
        # Create the graph object and find optimal MIS
        G = graph_funcs.graph_from_file(graph)
        opt = helper_funcs.brute_force_search(G)

        # Read in the graph from the old file
        edge_list = []
        with open(graph, 'r') as gfile:
            for line in gfile:
                edge_list.append(line)

        if len(edge_list) == 1:
            edgestr = edge_list[0]
        else:
            raise Exception('More than 1 line in graph file')

        graph_dir = graph.split('/')[-2]
        graph_name = graph.split('/')[-1].strip('.txt')
        print(graph_dir,'-',graph_name, 'opt =', opt)

        # Convert the edges to a list of tups
        all_edges = []
        for edge in edgestr.split(')'):
            edge_pair = [int(n) for n in edge.strip(' ,(').split(',') if n != '']
            if len(edge_pair) > 0:
                all_edges.append(edge_pair)

        num_nodes = 0
        for edge in all_edges:
            for node in edge:
                if node > num_nodes:
                    num_nodes = node
        num_nodes += 1
        print('\tp', num_nodes, len(all_edges))

        # Write the graph to the new file
        if not os.path.isdir(graph_dir):
            os.mkdir(graph_dir)
        with open(graph_dir + '/' + graph_name + '.txt', 'w') as savefile:
            savefile.write('p {} {}\n'.format(num_nodes, len(all_edges)))
            savefile.write('c Optimal MIS = {}\n\n'.format(opt))

            for edge in all_edges:
                savefile.write('{} {}\n'.format(edge[0], edge[1]))
                savefile.write('{} {}\n'.format(edge[1], edge[0]))
                savefile.write('\n')



