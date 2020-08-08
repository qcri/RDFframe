from rdfframes.knowledge_graph import KnowledgeGraph
from rdfframes.utils.constants import JoinType

graph = KnowledgeGraph(graph_name='dbpedia')


def expand_join(join_type):
    basketball_palyer = graph.entities('dbpo:BasketballPlayer', entities_col_name='player')\
        .expand('player', [('dbpp:nationality', 'nationality'), ('dbpp:birthPlace', 'place'),
                           ('dbpp:birthDate', 'birthDate'), ('dbpp:team', 'team')])
    basketball_team = graph.entities('dbpo:BasketballTeam', entities_col_name='team')\
        .expand('team', [('dbpp:president', 'president'), ('dbpp:sponsor', 'sponsor'), ('dbpp:name', 'name')])
    basketball_palyer_team = basketball_team.join(basketball_palyer,'team', join_type=join_type)
    print(basketball_palyer_team.to_sparql())


expand_join(JoinType.InnerJoin) ## change the type here.


