#include <iostream>
#include <vector>
#include <fstream>
#include <istream>
#include <string>
#include <sstream>
#include <algorithm>


std::vector<std::vector<int>> readDimacsGraph(std::istream &infile)
{
    int numVertices;
    int numEdges;
    std::string line;
    while (getline(infile, line))
    {
        std::istringstream iss(line);
        char firstSymbol;
        if (!(iss >> firstSymbol))
        {
            break;
        } // error

        if (firstSymbol == 'p')
        {
            std::string td;
            iss >> td >> numVertices >> numEdges;
            break;
        }
    }

    std::vector<std::vector<int>> graph(numVertices);

    while (getline(infile, line))
    {
        if (line.empty())
        {
            continue;
        }

        if (line[0] == 'c')
        {
            continue;
        }

        std::istringstream iss(line);

        int u, v;
        char p;
        iss >> p >> u >> v;

        --u;
        --v;

        if (u < 0 || u >= numVertices)
        {
            std::cout << "Invalid node ID: " << u << std::endl;
            exit(1);
        }
        if (v < 0 || v >= numVertices)
        {
            std::cout << "Invalid node ID: " << v << std::endl;
            exit(1);
        }

        if (u == v)
        {
            continue;
        }

        if (std::find(graph[u].begin(), graph[u].end(), v) == graph[u].end())
        {
            graph[u].push_back(v);
        }

        if (std::find(graph[v].begin(), graph[v].end(), u) == graph[v].end())
        {
            graph[v].push_back(u);
        }
    }

    for (int i = 0; i < numVertices; ++i)
    {
        std::sort(graph[i].begin(), graph[i].end());
    }

    return graph;
}

std::vector<std::vector<int>> readDimacsGraphFromFile(std::string fileName)
{
    std::ifstream fin(fileName);
    return readDimacsGraph(fin);
}

std::vector<std::vector<int>> readDimacsGraphFromCin()
{
    return readDimacsGraph(std::cin);
}