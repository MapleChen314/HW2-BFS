# write tests for bfs
import pytest
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    gfile='./data/tiny_network.adjlist'
    tiny_graph=graph.Graph(gfile)
    test_var=tiny_graph.bfs("Michael Keiser")
    assert len(test_var)==30
    assert test_var[0]=="Michael Keiser"

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    gfile='./data/citation_network.adjlist'
    citation_graph=graph.Graph(gfile)
    test_var=citation_graph.bfs("Michael Keiser", "Lani Wu")
    assert test_var==['Michael Keiser', '33232663', 'Bruce Conklin', '30814728', 'Lani Wu']

def test_unconnected():
    '''
    This tests whether unconnected start and end nodes will return None.
    '''
    gfile='./data/citation_network.adjlist'
    citation_graph=graph.Graph(gfile)
    test_var=citation_graph.bfs("Lani Wu","Alexander (Sandy) Johnson")
    assert test_var==None
    
def test_empty():
    gfile='./data/empty.adjlist'
    empty_graph=graph.Graph(gfile)
    with pytest.raises(ValueError):
        empty_graph.bfs("Lani Wu")

def test_nonexist():
    gfile='./data/tiny_network.adjlist'
    empty_graph=graph.Graph(gfile)
    with pytest.raises(ValueError):
        empty_graph.bfs("Maple Chen")