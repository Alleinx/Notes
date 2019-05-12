import java.util.Date;

public class Note {
	private String content;
	private Date time;
	private Brew brew;

	public Note() {
		brew = new Brew(this);
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	public Date getTime() {
		return time;
	}

	public void setTime(Date time) {
		this.time = time;
	}

	public Brew getBrew() {
		return brew;
	}
}
