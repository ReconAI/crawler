// jsx code
'use strict';

class ResultItem extends React.Component {
    constructor(props) {
        super(props);
        this.handlePlayClick = this.handlePlayClick.bind(this);
        this.handlePauseClick = this.handlePauseClick.bind(this);
    }
    handlePlayClick() {
        let video_id = document.getElementById("video_"+this.props.item.id);
        video_id.play();
    }

    handlePauseClick() {
        let video_id = document.getElementById("video_"+this.props.item.id);
        video_id.pause();
    }

  render () {
    return (
        <div className='row border col-sm-12 col-md-12 col-lg-12 resultItem'>
                <div className='col-sm-6'>
                    <div className='row'>
                        <div className='col-sm-10'>
                            <p className='h5'><a href={this.props.item.source_link}>{this.props.item.source_link}</a></p>
                            <div className='embed-responsive embed-responsive-16by9'>
                                <video id={"video_"+this.props.item.id}>
                                 <source src={this.props.item.preview_link} type="video/ogg"/>
                                </video>
                            </div>
                        </div>
                        <div
                            className='col-sm-2 col-md-2 col-lg-2 d-flex flex-column justify-content-center align-items-start'>
                            <button type='button' className='btn btn-outline-secondary player-button'><img src='static/img/player.svg' onClick={this.handlePauseClick}/></button>
                            <button type='button' className='btn btn-outline-secondary'><img src='static/img/interface.svg' onClick={this.handlePlayClick}/></button>
                        </div>
                    </div>
                </div>
                <div className='col-sm-6 col-md-6 col-lg-6'>
                    <p className='h5'>Video details:</p>
                    <div className='container border video-details-wrapper1'>
                        <div className='video-details-wrapper2'>
                            <div className='video-details-wrapper3'>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    Parameter A
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    Parameter B
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    Parameter C
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    etc.
                                </label>
                            </div>
                            <div className='video-details-wrapper-values'>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    Value(s) A
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    Value(s) B
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    Value(s) C
                                </label>
                                <label className='form-check-label' htmlFor='defaultCheck1'>
                                    etc.
                                </label>
                            </div>
                        </div>
                    </div>
                    <div className='container video-details-button-wrapper'>
                        <button type='button' className='btn btn-secondary confirm-discard-button'>Confirm</button>
                        <button type='button' className='btn btn-secondary confirm-discard-button'>Discard</button>
                    </div>
                </div>
            </div>

    );
  }
}
class PrevNext extends React.Component {
  render() {
    return (
      <div>
        <a href={this.props.previous}>Previous</a> &nbsp;
        <a href={this.props.next}>Next</a>
      </div>
    );
  }
}

class SearchResult extends React.Component {
  render() {
    return (
        <div>
          {this.props.data['results'].map(item => {
            return <ResultItem item={item} key={item.source_link}/>
          })}
          <PrevNext next={this.props.data.next} prev={this.props.data.previous}/>
        </div>
    );
  }
}






