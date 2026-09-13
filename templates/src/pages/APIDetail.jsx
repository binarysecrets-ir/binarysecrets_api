import NavBar from "../components/Nav";
import BigIcon from "../components/bigIcon";
import Detail from "../components/Detail";

export default function APIDetail(){
    return(
        <div className="container">
        <NavBar />
        <BigIcon icon="image" />
        <Detail title="test" detail="cap" />
        </div>
    )
}
