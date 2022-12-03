import javax.sound.sampled.*;
public class Sound 
{
  public static void main(String[] args) 
  {
    playNote(Integer.parseInt(args[0]));
  }

  public static void playNote(double note) 
  {
    double hz = 440 * Math.pow(2, (note-4)/12);
    sine(hz);
  }

  public static void sine(double hz) 
  {
    System.out.println(hz);
    double sampleRate = 44100.0;
    double[] note = new double[50001];
    for (int i = 0; i <= 50000; i++)
    {
      note[i] = Math.sin(2*Math.PI*i*hz/sampleRate);
      note[i] = Math.sin(2*Math.PI*i*hz/sampleRate);
    }
    StdAudio.play(note);
  }
}
