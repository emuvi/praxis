package praxis.maven.jdbc;

import java.io.File;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class SQLiteTest {
    
    @Test
    public void createBase() throws Exception {
        String path = "test.db";
        File file = new File(path);
        file.delete();
        Assertions.assertEquals(false, file.exists());
        SQLite sqlite = new SQLite(path);
        sqlite.close();
        Assertions.assertEquals(true, file.exists());
        file.delete();
        Assertions.assertEquals(false, file.exists());
    }
}
