create table salon(salon_id int primary key, budget varchar(255), salon_name varchar(255), rating int, reviews int, website varchar(255), phone varchar(255), address varchar(255));
\copy salon from '~/Desktop/salon_data/salon.csv' delimiter ',' csv header;
create table amenities(salon_id int primary key, mask_required bool, accepts_card bool, accepts_andriod bool, accepts_apple bool, good_for_kids bool, car_parking bool, bike_parking bool, free_wifi bool, wheelchair_access bool, restrooms bool, appointments bool);
\copy amenities from '~/Desktop/salon_data/amenities.csv' delimiter ',' csv header;
create table services(salon_id int primary key, coloring bool, blowout bool, hair_treatment bool, kids_haircut bool, bridal_service bool, hair_extension bool, hairsyling bool, makeup bool, mens_haircut bool, womens_haircut bool);
\copy services from '~/Desktop/salon_data/services.csv' delimiter ',' csv header;
create table hours(salon_id int, day int, open varchar(255), close varchar(255));
\copy hours from '~/Desktop/salon_data/hours.csv' delimiter ',' csv header;