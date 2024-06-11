# Use the official MySQL 8.0 image from the Docker Hub
FROM mysql:8.0

# Set the environment variables for the MySQL root password
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=my_database
ENV MYSQL_USER=my_user
ENV MYSQL_PASSWORD=my_password

# Expose the default MySQL port
EXPOSE 3306

# Add a custom SQL script to the image
COPY ./init.sql /docker-entrypoint-initdb.d/

# Command to run the MySQL server
CMD ["mysqld"]