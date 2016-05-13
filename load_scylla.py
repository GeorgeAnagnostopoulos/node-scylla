from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('fci')

session.execute("CREATE TABLE dogs (dog_id int PRIMARY KEY, group text, section text, country text, dog_name text)")

session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (1, 'Scent_hounds', 'Large-sized Hounds', 'Belgium', 'CHIEN DE SAINT HUBERT (84) (BLOODHOUND)'))

session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (2, 'Scent hounds', 'Medium-sized Hounds', 'France', 'ARIEGEOIS (20)'))

session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (3, 'Scent hounds', 'Medium-sized Hounds', 'France', "CHIEN D'ARTOIS (28) (ARTOIS HOUND)"))
session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (4, 'Scent hounts', 'Medium-sized Hounds', 'France', 'BEAGLE HARRIER (290)'))
session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (5, 'Scent hounts', 'Medium-sized Hounts', 'France', 'GRIFFON BLEU DE GASCOGNE (32) (BLUE GASCONY GRIFFON)'))
session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (6, 'Scent hounts', 'Medium-sized Hounts', 'France', 'BRIQUET GRIFFON VENDEEN (19)'))

session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (7, 'Scent hounts', 'Medium-sized Hounts', 'Great Britain', 'HARRIER (295)'))

session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (8, 'Scent hounts', 'Medium-sized Hounts', 'Italy', 'SEGUGIO ITALIANO A PELO FORTE (198) (ITALIAN ROUGH-HAIRED SEGUGIO)'))
session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (9, 'Scent hounts', 'Medium-sized Hounts', 'Italy', 'SEGUGIO ITALIANO A PELO RASO (337) (ITALIAN SHORT-HAIRED SEGUGIO)'))


session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (10, 'Scent hounts', 'Small-sized Hounts', 'Germany', 'DEUTSCHE BRACKE (299) (GERMAN HOUND)'))

session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (11, 'Scent hounts', 'Small-sized Hounts', 'Germany', 'WESTFALISCHE DACHSBRACKE (100) (WESTPHALIAN DACHSBRACKE)'))

session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (12, 'Scent hounts', 'Small-sized hounts', 'Great Britain', 'BASSET HOUND'))
session.execute("INSERT INTO dogs (dog_id, group, section, country, dog_name) VALUES (%s, %s, %s, %s, %s)", (13, 'Scent Hounts', 'Small-sized Hounts', 'Great Britain', 'BEAGLE (161)'))
