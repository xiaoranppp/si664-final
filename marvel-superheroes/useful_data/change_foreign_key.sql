

ALTER TABLE character_power
            DROP FOREIGN KEY character_power_ibfk_1,
            DROP FOREIGN KEY character_power_ibfk_2;

ALTER TABLE character_power
            ADD CONSTRAINT character_info_fk_character_id
                           FOREIGN KEY (character_id)
                           REFERENCES character_info(character_id)
                           ON DELETE CASCADE ON UPDATE CASCADE,
            ADD CONSTRAINT power_fk_power_id
                           FOREIGN KEY (power_id)
                           REFERENCES power(power_id)
                           ON DELETE CASCADE ON UPDATE CASCADE
ALTER TABLE character_comic
            DROP FOREIGN KEY character_comic_ibfk_1,
            DROP FOREIGN KEY character_comic_ibfk_2;
ALTER TABLE character_comic
            ADD CONSTRAINT comic_fk_comic_id
                           FOREIGN KEY (comic_id)
                           REFERENCES comic(comic_id)
                           ON DELETE CASCADE ON UPDATE CASCADE;