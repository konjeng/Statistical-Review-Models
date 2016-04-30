import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.StringTokenizer;
import java.lang.OutOfMemoryError;

import edu.stanford.nlp.tagger.maxent.MaxentTagger;

public class tagText {
	// JDBC driver name and database URL
	static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
	static final String DB_URL = "jdbc:mysql://localhost/review_system";

	// Database credentials
	static final String USER = "root";
	static final String PASS = "root";

	static void findPOC(String s, Long sentenceId) throws ClassNotFoundException, SQLException {

		String[] Stringparts = s.split("/");

		Connection conn = null;
		Statement stmt = null;
		java.sql.PreparedStatement ps = null;

		Class.forName("com.mysql.jdbc.Driver");
		conn = (Connection) DriverManager.getConnection(DB_URL, USER, PASS);
		stmt = (Statement) conn.createStatement();

		String sql = "INSERT INTO tag_word VALUES(NULL,?,?,?)";
		ps = conn.prepareStatement(sql);
		ps.setString(1, Stringparts[0]);
		ps.setString(2, Stringparts[1]);
		ps.setLong(3, sentenceId);
		ps.executeUpdate();
		stmt.close();
		conn.close();
	}

	public static void main(String[] args) throws IOException, ClassNotFoundException, SQLException {

		// Initialize the tagger
		MaxentTagger tagger = new MaxentTagger("taggers/bidirectional-distsim-wsj-0-18.tagger");

		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;

		Class.forName("com.mysql.jdbc.Driver");
		conn = (Connection) DriverManager.getConnection(DB_URL, USER, PASS);
		stmt = (Statement) conn.createStatement();

		String sql = "SELECT id,review_sentence from review_sentence";
		rs = stmt.executeQuery(sql);

		String reviewsentence;
		String taggedReview;
		Long id;
		while (rs.next()) {
			try{
				id = rs.getLong("id");
				System.out.println("id=" + id);
				reviewsentence = rs.getString("review_sentence");
				reviewsentence = reviewsentence.replaceAll("[^a-zA-Z0-9 '-]", " ");
				taggedReview = tagger.tagString(reviewsentence);

//				System.out.println(taggedReview);
				StringTokenizer st = new StringTokenizer(taggedReview);
				while (st.hasMoreTokens()) {
					String term = st.nextToken();
//					System.out.println(term);
					findPOC(term, id);
				}
				System.out.println("");
			}
			catch(OutOfMemoryError e){
				System.out.println("Unable to process review. String too long.");
			}
			catch(Exception e){
				System.out.println("Error!!!!!");
			}
		}
	}
}
