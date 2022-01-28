import os
uri = 'clickhouse://default:@10.10.25.106:8123/plato_idx_slave'
# uri = 'clickhouse://default:@10.10.23.103:8123/plato_materialized_view'

from urllib.parse import quote_plus
output_dir = '/home/sxg/code/github/sqlacodegen/test-tables'
tables = ["DM_PORT_ASSET", 'DM_PORT_POSITION', 'INFO_IDX_EODVALUE', 'INFO_IDX_BASICINFO']

# password = 'Sxg!@#123'
# uri = "mysql+pymysql://sxg:{}@101.43.135.141:3306/sys".format(quote_plus(password))
# tables = ["sys_config"]

sqlcodegen_path = '/home/sxg/code/github/sqlacodegen/src/sqlacodegen/__main__.py'


if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for table_name in tables:
    outfile = f'{table_name.lower()}.py'
    outfile = os.path.join(output_dir, outfile)
    command = f'python {sqlcodegen_path} --table {table_name} --noviews  --outfile {outfile} {uri}'
    print(command)
    ret = os.system(command)
    # print(ret)



# table_name = 'DIM_INFO'
# outfile = f'{table_name}.py'



# sqlcodegen_path = '/home/turing/workspace/sqlacodegen/src/sqlacodegen/__main__.py'
# # --table BOND_STOCK_FUND_MAPPING_LOCAL --noviews  --outfile BOND_STOCK_FUND_MAPPING_LOCAL.py clickhouse://default:@10.10.23.103:8123/plato_materialized_view


# # command = f'sqlacodegen --table {table_name} --noviews --noconstraints --noindexes --outfile {outfile} {uri}'
# # command = f'sqlacodegen --table {table_name} --noviews  --outfile {outfile} {uri}'
# command = f'python {sqlcodegen_path} --tables {table_name} --noviews  --outfile {outfile} {uri}'
# # outfile = '/home/turing/workspace/repo/models/all_model.py'
# # command = f'python {sqlcodegen_path}   --noviews  --outfile {outfile} {uri}'
# print(command)
# ret = os.system(command)
# print(ret)
