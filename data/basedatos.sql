
# GRANT ALL PRIVILEGES ON iot_info.* TO '<usr>'@'localhost' IDENTIFIED BY '<pwd>';

CREATE DATABASE iot_info;

CREATE TABLE sensores_data (
	idSD INT AUTO_INCREMENT PRIMARY KEY,
	Fecha datetime not null,
	data JSON not null
)ENGINE=InnoDB;
