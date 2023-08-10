package praxis.maven.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;

public class PostgreSQL implements AutoCloseable {
 
    private Connection connection;
    
    public PostgreSQL(String host, Integer port, String base, String user, String pass) throws Exception {
        Class.forName("org.postgresql.Driver");
        connection = DriverManager.getConnection("jdbc:postgresql://" + host + ":" + port + "/" + base, user, pass);
    }

    @Override
    public void close() throws Exception {
        connection.close();
    }

}
