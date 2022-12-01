from .entities.entity import Session, engine, Base
from .entities.match import Match

Base.metadata.create_all(engine)

session = Session()

matches = session.query(Match).all()

if len(matches) == 0:
    test_match = Match("1", "BlueTop", "BlueJg", "BlueMid", "BlueBot", "BlueSup", "RedTop", "RedJg", "RedMid", "RedBot", "RedSup", "script")
    session.add(test_match)
    session.commit()
    session.close()
    
    matches = session.query(Match).all()
    
print('### Matches')
for match in matches:
    print(f"{match.id} - {match.match_id} / {match.last_updated_by}")