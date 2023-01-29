from codemap import schemas
from neo4j import Transaction


def query_all_codesets(tx: Transaction):
    query = """
        MATCH
            (a:Code)-[:BELONGS_TO]->(b:CodeSet)
        RETURN a, b
        ORDER BY a.key
    """
    data = list(tx.run(query))
    return data


def handle_get_codeset_by_name(tx, name: str):
    query = """
        MATCH
            (a:Code)-[:BELONGS_TO]->(b:CodeSet)
        WHERE b.name=$name
        RETURN a, b
        ORDER BY a.key
    """
    data = tx.run(query, name=name)
    return list(data)


def handle_create_codeset(tx, codeset: schemas.CodeSet):
    create_codeset_cypher = "CREATE (cs: CodeSet {name: '$name'})"
    data = tx.run(create_codeset_cypher, name=codeset.name)
    return data


def handle_create_code(tx, code: schemas.Code):
    create_codes_cypher = f"""
        CREATE
            (c:Code {{key: '{code.key}', value: '{code.value}'}})
        RETURN c
    """
    return tx.run(create_codes_cypher)


def handle_link_code_to_codeset(tx, codeset: schemas.CodeSet, code: schemas.Code):
    create_code_relations_cypher = f"""
        MATCH
          (cs:CodeSet),
          (c:Code)
        WHERE cs.name = '{codeset.name}' AND c.key = '{code.key}'
        CREATE (c)-[r:BELONGS_TO]->(cs)
        RETURN c
    """
    return tx.run(create_code_relations_cypher)


def get_code_for_codeset(tx, codeset: schemas.CodeSet, code: schemas.Code):
    get_codeset_with_code = f"""
        MATCH
            (cs: CodeSet)<-[r]-(c: Code)
        WHERE
            cs.name = '{codeset.name}'
            AND TYPE(r) = 'BELONGS_TO'
            AND c.key = '{code.key}'
        RETURN c
    """
    data = tx.run(get_code_for_codeset)
    return data
