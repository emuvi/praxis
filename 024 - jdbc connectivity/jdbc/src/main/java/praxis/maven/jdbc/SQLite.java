package praxis.maven.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;

public class SQLite implements AutoCloseable {
    
    private Connection connection;

    public SQLite(String path) throws Exception {
        Class.forName("org.sqlite.JDBC");
        connection = DriverManager.getConnection("jdbc:sqlite:" + path);
    }

    @Override
    public void close() throws Exception {
        connection.close();
    }

}
