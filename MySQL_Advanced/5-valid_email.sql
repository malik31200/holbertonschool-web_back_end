-- Reset valid_email when email changes

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
SET NEW.valid_email = CASE
    WHEN OLD.email <> NEW.email THEN 0
    ELSE NEW.valid_email
END;