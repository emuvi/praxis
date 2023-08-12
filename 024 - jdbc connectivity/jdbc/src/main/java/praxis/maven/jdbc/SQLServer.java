package praxis.maven.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;

public class SQLServer implements AutoCloseable {
 
    private Connection connection;
    
    public SQLServer(String host, Integer port, String base, String user, String pass) throws Exception {
        Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
        connection = DriverManager.getConnection("jdbc:sqlserver://" + host + ":" + port + ";databaseName=" + base, user, pass);
    }

    @Override
    public void close() throws Exception {
        connection.close();
    }

}
