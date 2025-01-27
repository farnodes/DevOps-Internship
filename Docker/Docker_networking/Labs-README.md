### Docker Networking

1. Explore the current setup and identify the number of networks that exist on this system.

2. What is the ID associated with the bridge network?

3. We just ran a container named alpine-1. Identify the network it is attached to.

4. What is the subnet configured on bridge network?

5. Run a container named alpine-2 using the alpine image and attach it to the none network.

6. Create a new network named wp-mysql-network using the bridge driver. Allocate subnet 182.18.0.0/24. Configure Gateway 182.18.0.1

7. Deploy a mysql database using the mysql:5.6 image and name it mysql-db. Attach it to the newly created network wp-mysql-network. Set the database password to use db_pass123. The environment variable to set is MYSQL_ROOT_PASSWORD.

8. Deploy a web application named webapp using the kodekloud/simple-webapp-mysql image. Expose the port to 38080 on the host.

   The application makes use of two environment variable:
   1: DB_Host with the value mysql-db.
   2: DB_Password with the value db_pass123.
   Make sure to attach it to the newly created network called wp-mysql-network.


   Also make sure to link the MySQL and the webapp container.




















































