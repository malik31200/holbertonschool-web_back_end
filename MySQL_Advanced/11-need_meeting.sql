-- View that displays the students that have a score under 80 
-- and  and no last_meeting or more than 1 month.
CREATE VIEW need_meeting AS
SELECT name
from students
WHERE score < 80
AND (
    last_meeting IS NULL
    OR last_meeting IS NULL
    OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
);