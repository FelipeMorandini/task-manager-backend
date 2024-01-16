from sqlalchemy.orm import Session

class BaseRepository:

    def __init__(self, model):
        self.model = model

    """
    Retrieves a single record from the database based on the provided id.

    Parameters:
        db (Session): The database session object.
        id (int): The id of the record to retrieve.

    Returns:
        The first record that matches the provided id.
    """
    def get(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.id == id).first()

    
    """
    Retrieves all records from the database.

    Args:
        db (Session): The database session.

    Returns:
        List[Model]: A list of all records from the database.
    """
    def get_all(self, db: Session): 
        return db.query(self.model).all()

    
    """
    Create a new object in the database.

    Parameters:
        db (Session): The database session.
        obj (dict): The object to be created.

    Returns:
        db_obj: The created object.
    """
    def create(self, db: Session, obj: dict):
        db_obj = self.model(**obj)  
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    
    """
    Updates an object in the database.

    Args:
        db (Session): The database session.
        obj (dict): The object to be updated.

    Returns:
        dict: The updated object.
    """
    def update(self, db: Session, obj: dict):
        db.query(self.model).filter(self.model.id == obj['id'])\
            .update(obj)
        db.commit()
        return obj

    
    """
    Delete a record from the database.

    Parameters:
        db (Session): The database session object.
        id (int): The ID of the record to be deleted.

    Returns:
        The deleted database object.
    """
    def delete(self, db: Session, id: int):
        db_obj = db.query(self.model).get(id)
        db.delete(db_obj)
        db.commit()
        return db_obj